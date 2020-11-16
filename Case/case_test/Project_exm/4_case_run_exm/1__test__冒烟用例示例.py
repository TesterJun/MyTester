import default_keywords as public

# ============================
public.setup()
# ============================
public.make_file('dir_name_1/dir_name_1', 'file_name_1', 'test_word', '')

# ============================
public.step()
# ============================
public.get_dir_info('dir_name_1/dir_name_1', '')
public.save_data('__public__', 'dir_info', 'test_info')
public.find_from_info('test_info', 'file_name_1', '')

# ============================
public.teardown()
# ============================
public.remove('dir_name_1/dir_name_1', 'file_name_1', 'file', '')