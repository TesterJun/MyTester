import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', 'COURSE_ID', appKey='', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_ID', appKey='S_STR', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_ID', appKey='NO_EXIST_USERID', is_assert='2')

# ============================
public.teardown()
# ============================