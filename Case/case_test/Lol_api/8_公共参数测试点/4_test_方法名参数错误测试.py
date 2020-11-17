import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', 'COURSE_01', method='', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_01', method='TEST_STR_01', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_01', method='ERROR_KEY_01', is_assert='2')

# ============================
public.teardown()
# ============================