import re
from apotekia.settings import ORDER_PREFIX
from sales.models import CustomerOrder


def generate_order_number():
    new_number = ''
    if CustomerOrder.objects.last():
        last_number = CustomerOrder.objects.last().number
        clean_number = re.sub(r'[azAZ]+', '', last_number)
        clean_number = int(clean_number)
        clean_number += 1
        new_number = ORDER_PREFIX + str(clean_number)
    else:
        number = int(1000001)
        new_number = ORDER_PREFIX + str(number)

    return new_number

