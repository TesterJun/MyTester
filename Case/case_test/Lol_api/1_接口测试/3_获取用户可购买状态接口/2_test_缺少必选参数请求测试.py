import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.canBuyCourse('lol_obj', 'COURSE_ID', 'USER_MOBILE', cancel_bizdata_key='courseId', is_assert='2')
lol.canBuyCourse('lol_obj', 'COURSE_ID', 'USER_MOBILE', cancel_bizdata_key='mobile', is_assert='2')

# ============================
public.teardown()
# ============================