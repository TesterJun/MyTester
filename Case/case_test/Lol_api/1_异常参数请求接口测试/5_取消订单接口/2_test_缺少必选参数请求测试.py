import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

lol.orderCreate(
    'lol_obj', 
    'COURSE_06', 
    'MOBILE_07', 
    'ORDER_04', 
    'TIME_STR_01',
    'ADDRESS_NAME',
    'ADDRESS_MOBILE',
    'ADDRESS_PROVINCE',
    'ADDRESS_CITY',
    'ADDRESS_AREA',
    'ADDRESS_ADDRESS'
)

# ============================
public.step()
# ============================

lol.orderCancel('lol_obj', 'ORDER_04', cancel_key='bizData', cancel_data_key='orderNo', is_assert='2')

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj', 'ORDER_04')