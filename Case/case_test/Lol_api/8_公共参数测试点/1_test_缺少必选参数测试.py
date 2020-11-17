import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', 'COURSE_01', cancel_key='appKey', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_01', cancel_key='module', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_01', cancel_key='method', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_01', cancel_key='bizData', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_01', cancel_key='requestId', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_01', cancel_key='sign', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_01', cancel_key='timestamp', is_assert='2')

# ============================
public.teardown()
# ============================