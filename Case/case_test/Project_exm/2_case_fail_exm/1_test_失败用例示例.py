import default_keywords as public

# ============================
public.setup()
# ============================
public.make_dir('', 'dir_name_1', '')

# ============================
public.step()
# ============================
public.make_file('dir_name_1', 'file_name_1', 'test_word', '')
public.get_dir_info('dir_name_1', '')
public.save_data('__public__', 'dir_info', 'test_key')

public.find_from_info('test_key', 'file_name_2', '')

# ============================
public.teardown()
# ============================
public.remove('', 'dir_name_1', 'dir', '')