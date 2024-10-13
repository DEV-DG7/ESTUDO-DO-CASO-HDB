project('task_manager', version: '1.0', default_options: ['warning_level=2', 'buildtype=release'])

# Importando o módulo Python
python = import('python')

# Encontrando a instalação do Python 3
py3 = python.find_installation('python3')

if not py3.found()
    error('Python 3.x não encontrado! Certifique-se de que está instalado corretamente.')
endif

# Definindo o caminho correto para o arquivo app.py
src_files = ['app.py'] # Agora o app.py está no diretório raiz

# Instalando arquivos Python
py3.install_sources(src_files)

# Testes automatizados
test('python_test_suite', py3, args: ['-m', 'unittest', 'discover', 'test'])

# Copiando outros arquivos necessários para o diretório de instalação
install_data('requirements.txt', install_dir: get_option('datadir') / 'task_manager')

message('Build configurado com sucesso para Task Manager!')
