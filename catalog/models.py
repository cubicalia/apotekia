from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from apotekia.utils import get_image_upload_path


class ProductCategory(models.Model):
    name = models.CharField(_('Name'), max_length=255, blank=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               blank=True, null=True, related_name='children')

    class Meta:
        verbose_name_plural = _("Categories")

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Product(models.Model):
    title = models.CharField(_('Name'),
                             max_length=128)
    # Properties
    active = models.BooleanField(_("Active"),
                                 default=True, help_text=_("Is this product publicly visible."),)
    track_stock = models.BooleanField(_("Track stock levels?"),
                                      default=True)
    is_discountable = models.BooleanField(_("Is discountable?"),
                                          default=True, help_text=_(
        "This flag indicates if this product can be used in an offer "
        "or not"))
    description = models.TextField(_('Description'),
                                   blank=True)
    date_created = models.DateTimeField(_("Date created"),
                                        auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(_("Date updated"),
                                        auto_now=True, db_index=True)
    # Product values
    upc = models.CharField(_("UPC"),
                           max_length=64, blank=True, null=True, unique=True,
                           help_text=_("Universal Product Code (UPC) is an identifier for "
                                       "a product which is not specific to a particular "
                                       " supplier. Eg an ISBN for a book."))
    length = models.DecimalField(_('Product length dimension'),
                                 blank=True, null=True, max_digits=6, decimal_places=2)
    width = models.DecimalField(_('Product width dimension'),
                                blank=True, null=True, max_digits=6, decimal_places=2)
    height = models.DecimalField(_('Product height dimension'),
                                 blank=True, null=True, max_digits=6, decimal_places=2)

    net_weight = models.DecimalField(_('Product net weight dimension'),
                                     blank=True, null=True, max_digits=6, decimal_places=2)
    gross_weight = models.DecimalField(_('Product gross weight dimension'),
                                       blank=True, null=True, max_digits=6, decimal_places=2)

    # Price and tax
    purchase_price = models.DecimalField(_('Purchase price'),
                                         blank=True, null=True, max_digits=6, decimal_places=2)
    selling_price = models.DecimalField(_('Selling price'),
                                        blank=True, null=True, max_digits=6, decimal_places=2)
    tax_rate = models.DecimalField(_('Tax Rate'), default=20.0, max_digits=5, decimal_places=2)

    category = models.ForeignKey(
        'catalog.ProductCategory',
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
        blank=True, null=True)

    suppliers = models.ManyToManyField('suppliers.Supplier', blank=True, verbose_name=_("Suppliers"))

    dci = models.CharField(_('DCI'), max_length=128, blank=True, null=True)
    prescription = models.CharField(_('Prescription'), max_length=128, blank=True, null=True)
    lab = models.CharField(_('Laboratory'), max_length=128, blank=True, null=True)
    th_class = models.CharField(_('Therapeutic Class'), max_length=128, blank=True, null=True)
    pharma_form = models.CharField(_('Pharmaceutical Form'), max_length=128, blank=True, null=True)
    tableau = models.CharField(_('Tableau'), max_length=128, blank=True, null=True)
    marketable = models.CharField(_('Marketable'), max_length=128, blank=True, null=True)
    refundable = models.BooleanField(_('Refundable'), default=True, blank=True, null=True)
    adult_dosage = models.TextField(_('Adult Dosage'), blank=True, null=True)
    child_dosage = models.TextField(_('Child Dosage'), blank=True, null=True)
    driving_indication = models.TextField(_('Driving Indication'), blank=True, null=True)
    baby_feeding_indication = models.TextField(_('Baby Feeding Indication'), blank=True, null=True)
    pregnancy_indication = models.TextField(_('Pregnancy Indication'), blank=True, null=True)

    class Meta:
        app_label = 'catalog'
        ordering = ['title']
        verbose_name = _("Product")
        verbose_name_plural = _("Product")

    def __str__(self):
        return self.title

    def get_all_images(self):
        return self.images.all()

    def primary_image(self):
        """
        Returns the primary image for a product. Usually used when one can
        only display one product image, e.g. in a list of products.
        """
        images = self.get_all_images()
        ordering = self.images.model.Meta.ordering
        if not ordering or ordering[0] != 'display_order':
            # Only apply order_by() if a custom model doesn't use default
            # ordering. Applying order_by() busts the prefetch cache of
            # the ProductManager
            images = images.order_by('display_order')
            return images[0]


class ProductImage(models.Model):
    product = models.ForeignKey('catalog.Product',
                                on_delete=models.CASCADE,
                                related_name='images',
                                verbose_name=_("Product"))
    original = models.ImageField(
        _("Original"), upload_to=get_image_upload_path, max_length=255)
    caption = models.CharField(_("Caption"), max_length=200, blank=True)
    display_order = models.PositiveIntegerField(
        _("Display order"), default=0, db_index=True,
        help_text=_("An image with a display order of zero will be the primary"
                    " image for a product"))
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)

    class Meta:
        app_label = 'catalog'
        # Any custom models should ensure that this ordering is unchanged, or
        # your query count will explode. See AbstractProduct.primary_image.
        ordering = ["display_order"]
        verbose_name = _('Product image')
        verbose_name_plural = _('Product images')

    def __str__(self):
        return "Image of '%s'" % self.product

    def is_primary(self):
        """
        Return bool if image display order is 0
        """
        return self.display_order == 0

    def delete(self, *args, **kwargs):
        """
        Always keep the display_order as consecutive integers. This avoids
        issue #855.
        """
        super().delete(*args, **kwargs)
        for idx, image in enumerate(self.product.images.all()):
            image.display_order = idx
            image.save()

