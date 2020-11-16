import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderCancel('lol_obj', '', is_assert='2')
lol.orderCancel('lol_obj', 'S_STR', is_assert='2')
lol.orderCancel('lol_obj', 'NO_EXIST_ORDERID', is_assert='2')

# ============================
public.teardown()
# ============================