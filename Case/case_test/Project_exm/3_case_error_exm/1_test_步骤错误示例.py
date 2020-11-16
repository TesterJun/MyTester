import default_keywords as public

# ============================
public.setup()
# ============================
public.make_dir('', 'dir_name_1', '')

# ============================
public.step()
# ============================
public.make_file('dir_name_1/dir_name_2', 'file_name_1', 'test_word', '')
public.input_file('dir_name_1', 'file_name_1', 'test_word', '')

# ============================
public.teardown()
# ============================
public.remove('', 'dir_name_1', 'dir', '')