project('task_manager', 'python',
  version : '1.0',
  default_options : ['warning_level=3']
)

python = import('python').find_installation('python3')

py_mod = python.extension_module('task_manager', 'src/app.py')

test('unit', py_mod, args : ['-m', 'unittest', 'discover'])

python.install_sources('src/',
  install_dir : join_paths(get_option('prefix'), 'lib', 'task_manager')
)
