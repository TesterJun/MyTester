import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.orderCreate('lol_obj', 'COURSE_3', 'MOBILE_1', 'ORDER_2', 'TIME_STR_1', 'jun', 'MOBILE_1', '北京', '北京', '门头沟', '测试地址')
lol.orderCreate('lol_obj', 'COURSE_3', 'MOBILE_1', 'ORDER_2', 'TIME_STR_1', 'jun', 'MOBILE_1', '北京', '北京', '门头沟', '测试地址', is_assert='2')

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj', 'ORDER_2')