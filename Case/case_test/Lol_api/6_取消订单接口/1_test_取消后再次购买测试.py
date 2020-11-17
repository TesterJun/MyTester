import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

lol.make_order('lol_obj')

# ============================
public.step()
# ============================

lol.orderCreate('lol_obj', 'COURSE_01', 'MOBILE_03', 'TIME_STR_01', 'ADDRESS_NAME', 'ADDRESS_MOBILE', 'ADDRESS_PROVINCE', 'ADDRESS_CITY', 'ADDRESS_AREA', 'ADDRESS_ADDRESS')
lol.orderCancel('lol_obj')
lol.make_order('lol_obj')
lol.orderCreate('lol_obj', 'COURSE_01', 'MOBILE_03', 'TIME_STR_01', 'ADDRESS_NAME', 'ADDRESS_MOBILE', 'ADDRESS_PROVINCE', 'ADDRESS_CITY', 'ADDRESS_AREA', 'ADDRESS_ADDRESS')

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj')