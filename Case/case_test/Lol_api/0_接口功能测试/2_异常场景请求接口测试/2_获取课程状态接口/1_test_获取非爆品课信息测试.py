import default_keywords as public
import lol_keywords as lol

# ============================
public.setup()
# ============================

# ============================
public.step()
# ============================

lol.getCourseSaleStatus('lol_obj', 'NO_TEST_ID_1', is_assert='2')
lol.getCourseSaleStatus('lol_obj', 'NO_TEST_ID_2', is_assert='2')

# ============================
public.teardown()
# ============================