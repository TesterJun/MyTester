import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.canBuyCourse('lol_obj', 'COURSE_01', '', is_assert='2')
lol.canBuyCourse('lol_obj', 'COURSE_01', 'TEST_STR_01', is_assert='2')
lol.canBuyCourse('lol_obj', 'COURSE_01', 'MOBILE_04', is_assert='2')
lol.canBuyCourse('lol_obj', 'COURSE_01', 'MOBILE_05', is_assert='2')
lol.canBuyCourse('lol_obj', 'COURSE_01', 'MOBILE_06', is_assert='2')

# ============================
public.teardown()
# ============================