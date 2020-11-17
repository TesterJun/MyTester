import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderSuccess('lol_obj', 'ORDER_06', 'TIME_STR_01', cancel_key='bizData', cancel_data_key='orderNo', is_assert='2')
lol.orderSuccess('lol_obj', 'ORDER_06', 'TIME_STR_01', cancel_key='bizData', cancel_data_key='payTime', is_assert='2')

# ============================
public.teardown()
# ============================