import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================
lol.make_order('lol_obj')
# ============================
public.step()
# ============================

lol.orderCancel('lol_obj', is_assert='2')

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj')