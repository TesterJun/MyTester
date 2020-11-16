import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', 'COURSE_ID', cancel_key='appKey', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_ID', cancel_key='module', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_ID', cancel_key='method', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_ID', cancel_key='bizData', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_ID', cancel_key='requestId', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_ID', cancel_key='sign', is_assert='2')

# ============================
public.teardown()
# ============================