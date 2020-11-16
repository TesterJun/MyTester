import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', 'COURSE_ID', method='', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_ID', method='S_STR', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_ID', method='NO_EXIST_METHOD', is_assert='2')

# ============================
public.teardown()
# ============================