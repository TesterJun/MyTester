import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', '', is_assert='2')
lol.getCourseInfo('lol_obj', 'S_STR', is_assert='2')
lol.getCourseInfo('lol_obj', 'NO_EXIST_COURSEID', is_assert='2')

# ============================
public.teardown()
# ============================