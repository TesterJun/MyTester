import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseSaleStatus('lol_obj', 'COURSE_01', cancel_key='bizData', cancel_data_key='courseId', is_assert='2')

# ============================
public.teardown()
# ============================