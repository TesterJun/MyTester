import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.canBuyCourse('lol_obj', '', 'MOBILE_01', is_assert='2')
lol.canBuyCourse('lol_obj', 'TEST_STR_01', 'MOBILE_01', is_assert='2')
lol.canBuyCourse('lol_obj', 'abcd', 'MOBILE_01', is_assert='2')

# ============================
public.teardown()
# ============================