import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseInfo('lol_obj', 'COURSE_ID', cancel_bizdata_key='courseId', is_assert='2')

# ============================
public.teardown()
# ============================