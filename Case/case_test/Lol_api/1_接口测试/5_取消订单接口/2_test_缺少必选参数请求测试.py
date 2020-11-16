import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderCancel('lol_obj', 'ORDER_ID', cancel_bizdata_key='orderNo', is_assert='2')

# ============================
public.teardown()
# ============================