import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderCreate('lol_obj', 'COURSE_06', 'MOBILE_03', 'ORDER_02', 'TIME_STR_01', 'ADDRESS_NAME', 'ADDRESS_MOBILE', 'ADDRESS_PROVINCE', 'ADDRESS_CITY', 'ADDRESS_AREA', 'ADDRESS_ADDRESS')
lol.orderCancel('lol_obj', 'ORDER_02')
lol.orderCreate('lol_obj', 'COURSE_06', 'MOBILE_03', 'ORDER_02', 'TIME_STR_01', 'ADDRESS_NAME', 'ADDRESS_MOBILE', 'ADDRESS_PROVINCE', 'ADDRESS_CITY', 'ADDRESS_AREA', 'ADDRESS_ADDRESS')

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj', 'ORDER_02')