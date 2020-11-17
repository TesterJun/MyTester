import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.canBuyCourse('lol_obj', '', 'USER_MOBILE', is_assert='2')
lol.canBuyCourse('lol_obj', 'S_STR', 'USER_MOBILE', is_assert='2')
lol.canBuyCourse('lol_obj', 'NO_EXIST_COURSEID', 'USER_MOBILE', is_assert='2')

# ============================
public.teardown()
# ============================