import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderCreate('lol_obj', 'NO_TEST_ID_4', 'MOBILE_1', 'ORDER_2', 'TIME_STR_1', 'jun', '18614032279', '北京', '北京', '门头沟', '测试地址', is_assert='2')
lol.orderCreate('lol_obj', 'NO_TEST_ID_1', 'MOBILE_1', 'ORDER_2', 'TIME_STR_1', 'jun', '18614032279', '北京', '北京', '门头沟', '测试地址', is_assert='2')
lol.orderCreate('lol_obj', 'NO_TEST_ID_2', 'MOBILE_1', 'ORDER_2', 'TIME_STR_1', 'jun', '18614032279', '北京', '北京', '门头沟', '测试地址', is_assert='2')
lol.orderCreate('lol_obj', 'NO_TEST_ID_3', 'MOBILE_1', 'ORDER_2', 'TIME_STR_1', 'jun', '18614032279', '北京', '北京', '门头沟', '测试地址', is_assert='2')

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj', 'ORDER_2')