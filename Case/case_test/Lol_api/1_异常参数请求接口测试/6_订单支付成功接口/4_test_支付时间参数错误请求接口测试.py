import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderSuccess('lol_obj', 'ORDER_06', '', is_assert='2')
lol.orderSuccess('lol_obj', 'ORDER_06', 'S_STR_01', is_assert='2')
lol.orderSuccess('lol_obj', 'ORDER_06', 'TIME_STR_02', is_assert='2')

# ============================
public.teardown()
# ============================