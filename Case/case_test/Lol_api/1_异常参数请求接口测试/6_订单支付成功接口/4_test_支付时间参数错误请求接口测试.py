import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderSuccess('lol_obj', 'ORDER_ID', '', is_assert='2')
lol.orderSuccess('lol_obj', 'ORDER_ID', 'S_STR', is_assert='2')
lol.orderSuccess('lol_obj', 'ORDER_ID', 'NO_EXIST_TIMESTR', is_assert='2')

# ============================
public.teardown()
# ============================