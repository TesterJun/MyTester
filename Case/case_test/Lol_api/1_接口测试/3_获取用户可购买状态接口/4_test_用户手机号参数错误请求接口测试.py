import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.canBuyCourse('lol_obj', 'COURSE_ID', '', is_assert='2')
lol.canBuyCourse('lol_obj', 'COURSE_ID', 'S_STR', is_assert='2')
lol.canBuyCourse('lol_obj', 'COURSE_ID', 'NO_EXIST_USERMOBILE', is_assert='2')

# ============================
public.teardown()
# ============================