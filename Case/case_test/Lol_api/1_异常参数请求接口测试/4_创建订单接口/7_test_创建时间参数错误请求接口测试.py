import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderCreate(
    'lol_obj', 
    'COURSE_ID', 
    'USER_MOBILE', 
    'ORDER_ID', 
    '',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_address_key='name',
    is_assert='2'
)

lol.orderCreate(
    'lol_obj', 
    'COURSE_ID', 
    'USER_MOBILE', 
    'ORDER_ID', 
    'S_STR',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_address_key='name',
    is_assert='2'
)

lol.orderCreate(
    'lol_obj', 
    'COURSE_ID', 
    'USER_MOBILE', 
    'ORDER_ID', 
    'NO_EXIST_TIMESTR',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_address_key='name',
    is_assert='2'
)

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj', 'ORDER_ID')