import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderSuccess('lol_obj', '', 'TIME_STR_1', is_assert='2')
lol.orderSuccess('lol_obj', 'S_STR', 'TIME_STR_1', is_assert='2')
lol.orderSuccess('lol_obj', 'NO_EXIST_COURSE_ID', 'TIME_STR_1', is_assert='2')

# ============================
public.teardown()
# ============================