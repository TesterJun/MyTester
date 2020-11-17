import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', 'COURSE_01', timestamp='abcd', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_01', timestamp='TEST_STR_01', is_assert='2')

# ============================
public.teardown()
# ============================