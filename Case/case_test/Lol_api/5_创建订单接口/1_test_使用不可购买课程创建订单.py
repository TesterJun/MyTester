import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

lol.make_order('lol_obj')

# ============================
public.step()
# ============================

lol.orderCreate('lol_obj', 'COURSE_02', 'MOBILE_03', 'TIME_STR_01', 'ADDRESS_NAME', 'ADDRESS_MOBILE', 'ADDRESS_PROVINCE', 'ADDRESS_CITY', 'ADDRESS_AREA', 'ADDRESS_ADDRESS', is_assert='2')
lol.orderCreate('lol_obj', 'COURSE_03', 'MOBILE_03', 'TIME_STR_01', 'ADDRESS_NAME', 'ADDRESS_MOBILE', 'ADDRESS_PROVINCE', 'ADDRESS_CITY', 'ADDRESS_AREA', 'ADDRESS_ADDRESS', is_assert='2')
lol.orderCreate('lol_obj', 'COURSE_04', 'MOBILE_03', 'TIME_STR_01', 'ADDRESS_NAME', 'ADDRESS_MOBILE', 'ADDRESS_PROVINCE', 'ADDRESS_CITY', 'ADDRESS_AREA', 'ADDRESS_ADDRESS', is_assert='2')
lol.orderCreate('lol_obj', 'COURSE_05', 'MOBILE_03', 'TIME_STR_01', 'ADDRESS_NAME', 'ADDRESS_MOBILE', 'ADDRESS_PROVINCE', 'ADDRESS_CITY', 'ADDRESS_AREA', 'ADDRESS_ADDRESS', is_assert='2')

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj')