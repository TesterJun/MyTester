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
    '', 
    'MOBILE_03', 
    'TIME_STR_01',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    is_assert='2'
)

lol.orderCreate(
    'lol_obj', 
    'TEST_STR_01', 
    'MOBILE_03', 
    'TIME_STR_01',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    is_assert='2'
)

lol.orderCreate(
    'lol_obj', 
    'abcd', 
    'MOBILE_03', 
    'TIME_STR_01',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    is_assert='2'
)

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj')