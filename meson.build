project('task_manager', 'python', version: '1.0', default_options: ['warning_level=2', 'buildtype=release'])

# Importando o módulo Python
python = import('python')

# Encontre a instalação do Python
py3 = python.find_installation('python')

if not py3.found()
    error('Python 3.x não encontrado! Certifique-se de que está instalado corretamente.')
endif

# Diretório de origem do código
src_dir = 'src'

# Instalando arquivos Python
py3.install_sources(src_dir)

# Definindo um executável se necessário
executable('task_manager_exec', 'src/app.py', install: true)

# Testes automatizados (adaptar conforme necessário)
test('python_test_suite', py3, args: ['tests'])

# Copiando outros arquivos necessários para o diretório de instalação
install_data('requirements.txt', install_dir: get_option('datadir') / 'task_manager')

message('Build configurado com sucesso para Task Manager!')
