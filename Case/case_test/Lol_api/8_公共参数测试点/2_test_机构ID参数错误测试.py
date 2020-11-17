import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', 'COURSE_01', appKey='', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_01', appKey='TEST_STR_01', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_01', appKey='ERROR_KEY_01', is_assert='2')

# ============================
public.teardown()
# ============================