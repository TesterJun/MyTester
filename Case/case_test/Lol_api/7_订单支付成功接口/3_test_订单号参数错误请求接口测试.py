import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderSuccess('lol_obj', 'TIME_STR_01', orderNo='TEST_STR_01', is_assert='2')

# ============================
public.teardown()
# ============================