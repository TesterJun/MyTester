import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderCreate('lol_obj', 'COURSE_01', 'MOBILE_01', 'ORDER_01', 'TIME_STR_01', 'ADDRESS_NAME', 'ADDRESS_MOBILE', 'ADDRESS_PROVINCE', 'ADDRESS_CITY', 'ADDRESS_AREA', 'ADDRESS_ADDRESS')
lol.orderCreate('lol_obj', 'COURSE_01', 'MOBILE_01', 'ORDER_01', 'TIME_STR_01', 'ADDRESS_NAME', 'ADDRESS_MOBILE', 'ADDRESS_PROVINCE', 'ADDRESS_CITY', 'ADDRESS_AREA', 'ADDRESS_ADDRESS', is_assert='2')

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj', 'ORDER_01')