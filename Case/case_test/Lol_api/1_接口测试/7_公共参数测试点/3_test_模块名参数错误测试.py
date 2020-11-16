import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', 'COURSE_ID', module='', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_ID', module='S_STR', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_ID', module='NO_EXIST_MODULE', is_assert='2')

# ============================
public.teardown()
# ============================