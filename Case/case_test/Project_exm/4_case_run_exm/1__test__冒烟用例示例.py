import default_keywords

public = default_keywords

# ============================
public.setup()
# ============================
public.make_file('test_path/test_path', 'file_name_1', 'test_word', '')

# ============================
public.step()
# ============================
public.find('test_path/test_path', 'file_name_1', '')

# ============================
public.teardown()
# ============================
public.input_file('test_path/test_path', 'file_name_1', 'test_word', '')