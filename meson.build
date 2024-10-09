project('task_manager', 'python',
  version : '1.0',
  default_options : ['warning_level=3']
)

python = import('python').find_installation('python3')

# Module setup
py_mod = python.extension_module('task_manager', 'app.py')

# Unit test setup
test('unit', python, args : ['-m', 'unittest', 'discover'])

# Source installation setup
python.install_sources('src/',
  install_dir : join_paths(get_option('prefix'), 'lib', 'task_manager')
)
