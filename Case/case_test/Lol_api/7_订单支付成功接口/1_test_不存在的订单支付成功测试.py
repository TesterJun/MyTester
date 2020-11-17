import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================
lol.make_order('lol_obj')
# ============================
public.step()
# ============================

lol.orderSuccess('lol_obj', 'TIME_STR_01', is_assert="2")

# ============================
public.teardown()
# ============================