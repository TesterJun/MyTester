import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

lol.make_order('lol_obj')

# ============================
public.step()
# ============================

lol.orderCreate(
    'lol_obj', 
    'COURSE_01', 
    'MOBILE_03', 
    'TIME_STR_01',
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
    'COURSE_01', 
    'MOBILE_03', 
    'TIME_STR_01',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_address_key='mobile',
    is_assert='2'
)

lol.orderCreate(
    'lol_obj', 
    'COURSE_01', 
    'MOBILE_03', 
    'TIME_STR_01',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_address_key='province',
    is_assert='2'
)

lol.orderCreate(
    'lol_obj', 
    'COURSE_01', 
    'MOBILE_03', 
    'TIME_STR_01',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_address_key='city',
    is_assert='2'
)

lol.orderCreate(
    'lol_obj', 
    'COURSE_01', 
    'MOBILE_03', 
    'TIME_STR_01',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_address_key='area',
    is_assert='2'
)

lol.orderCreate(
    'lol_obj', 
    'COURSE_01', 
    'MOBILE_03', 
    'TIME_STR_01',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_address_key='address',
    is_assert='2'
)

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj')