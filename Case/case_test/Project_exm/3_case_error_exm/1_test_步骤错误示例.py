import default_keywords as public

# ============================
public.setup()
# ============================
public.make_dir('/', 'test_path', '')

# ============================
public.step()
# ============================
public.make_dir('/', 'test_path', '')
public.make_file('test_path/test_path', 'file_name_1', 'test_word', '')
public.find('test_path/test_path', 'file_name_2', '')
public.input_file('test_path/test_path', 'file_name_1', 'test_word', '')

# ============================
public.teardown()
# ============================
public.remove('/', 'test_path', 'dir', '')