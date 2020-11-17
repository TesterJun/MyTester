import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseSaleStatus('lol_obj', 'COURSE_03', is_assert='2')
lol.getCourseSaleStatus('lol_obj', 'COURSE_04', is_assert='2')

# ============================
public.teardown()
# ============================