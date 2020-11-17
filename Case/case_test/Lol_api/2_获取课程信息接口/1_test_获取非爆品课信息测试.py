import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', 'COURSE_02', is_assert='2')
lol.getCourseInfo('lol_obj', 'COURSE_03', is_assert='2')

# ============================
public.teardown()
# ============================