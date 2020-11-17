import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================
lol.make_order('lol_obj')
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
    'ADDRESS_ADDRESS'
)

# ============================
public.step()
# ============================

lol.orderCancel('lol_obj', cancel_key='bizData', cancel_data_key='orderNo', is_assert='2')

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj')