project('task_manager', 'c',
  version : '1.0',
  default_options : ['warning_level=3']
)

python = import('python').find_installation('python3')

# Testes unitários
test('unit', python, args : ['-m', 'unittest', 'discover'])

# Configuração de instalação
python.install_sources('src/',
  install_dir : join_paths(get_option('prefix'), 'lib', 'task_manager')
)
