import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderCancel('lol_obj', 'ORDER_03', is_assert='2')

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj', 'ORDER_03')