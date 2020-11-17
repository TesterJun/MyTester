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
    'TIME_STR_1',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_key='bizData', 
    cancel_data_key='courseId',
    is_assert='2'
)

lol.orderCreate(
    'lol_obj', 
    'COURSE_ID', 
    'USER_MOBILE', 
    'ORDER_ID', 
    'TIME_STR_1',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_key='bizData', 
    cancel_data_key='mobile',
    is_assert='2'
)

lol.orderCreate(
    'lol_obj', 
    'COURSE_ID', 
    'USER_MOBILE', 
    'ORDER_ID', 
    'TIME_STR_1',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_key='bizData', 
    cancel_data_key='orderNo',
    is_assert='2'
)

lol.orderCreate(
    'lol_obj', 
    'COURSE_ID', 
    'USER_MOBILE', 
    'ORDER_ID', 
    'TIME_STR_1',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_key='bizData', 
    cancel_data_key='createTime',
    is_assert='2'
)

lol.orderCreate(
    'lol_obj', 
    'COURSE_ID', 
    'USER_MOBILE', 
    'ORDER_ID', 
    'TIME_STR_1',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS',
    cancel_key='bizData', 
    cancel_data_key='address',
    is_assert='2'
)

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj', 'ORDER_ID')