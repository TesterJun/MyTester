import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderCancel('lol_obj', '123456789099999', is_assert='2')

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj', '123456789012345')