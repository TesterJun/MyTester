import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', '', is_assert='2')
lol.getCourseInfo('lol_obj', 'S_STR_01', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_05', is_assert='2')

# ============================
public.teardown()
# ============================