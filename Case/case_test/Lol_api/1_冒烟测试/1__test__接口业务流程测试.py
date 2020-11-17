import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

lol.make_order('lol_obj')

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', 'COURSE_01')
lol.getCourseSaleStatus('lol_obj', 'COURSE_01')
lol.canBuyCourse('lol_obj', 'COURSE_01', 'MOBILE_01')
lol.orderCreate(
    'lol_obj', 
    'COURSE_01', 
    'MOBILE_01', 
    'TIME_STR_01', 
    'ADDRESS_NAME', 
    'ADDRESS_MOBILE', 
    'ADDRESS_PROVINCE', 
    'ADDRESS_CITY', 
    'ADDRESS_AREA', 
    'ADDRESS_ADDRESS'
)
lol.orderCancel('lol_obj')

# ============================
public.teardown()
# ============================