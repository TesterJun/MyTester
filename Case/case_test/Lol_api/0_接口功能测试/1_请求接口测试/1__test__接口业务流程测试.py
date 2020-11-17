import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', 'COURSE_1')
lol.getCourseSaleStatus('lol_obj', 'COURSE_1')
lol.canBuyCourse('lol_obj', 'COURSE_1', 'MOBILE_1')
lol.orderCreate('lol_obj', 'COURSE_1', 'MOBILE_1', '123456789012345', 'TIME_STR_1', 'jun', '18614032279', '北京', '北京', '门头沟', '测试地址')
lol.orderCancel('lol_obj', '123456789012345')

# ============================
public.teardown()
# ============================
lol.orderCancel('lol_obj', '123456789012345')