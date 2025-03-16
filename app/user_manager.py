# Este arquivo gerencia os usuários do sistema
# Contém funções para autenticar, cadastrar e gerenciar os usuários logados

# Importa bibliotecas para trabalhar com arquivos JSON e sistema de arquivos
import json
import os

# Função que garante que a pasta de dados existe
def garantir_diretorio():
    # Verifica se a pasta "data" existe e a cria se não existir
    if not os.path.exists("data"):
        os.makedirs("data")

# Define o caminho do arquivo onde os dados dos usuários serão salvos
ARQUIVO_USUARIOS = "./data/usuarios.json"

def carregar_dados():
    """Carrega os dados de usuários do arquivo JSON."""
    # Garante que a pasta data existe
    garantir_diretorio()
    # Verifica se o arquivo de usuários existe
    if not os.path.exists(ARQUIVO_USUARIOS):
        return {}  # Retorna um dicionário vazio se o arquivo não existir
    try:
        # Abre o arquivo e carrega seu conteúdo
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Se houver erro ao ler o arquivo, retorna um dicionário vazio
        return {}

def salvar_dados(dados):
    """Salva os dados dos usuários no arquivo JSON."""
    # Garante que a pasta data existe
    garantir_diretorio()
    # Salva os dados no arquivo
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

def autenticar_usuario(nome, senha):
    """Verifica se o usuário e senha são válidos."""
    # Carrega os dados dos usuários
    dados_usuarios = carregar_dados()
    # Verifica se o nome de usuário existe e se a senha corresponde
    return nome in dados_usuarios and dados_usuarios[nome]['senha'] == senha

def cadastrar_usuario(nome, senha, email):
    """Cadastra um novo usuário, se ele ainda não existir."""
    # Carrega os dados dos usuários
    dados_usuarios = carregar_dados()
    # Verifica se o nome de usuário já existe
    if nome in dados_usuarios:
        return False  # Retorna falso se o usuário já existir
    # Adiciona o novo usuário ao dicionário
    dados_usuarios[nome] = {"senha": senha, "email": email}
    # Salva as alterações no arquivo
    salvar_dados(dados_usuarios)
    return True  # Retorna verdadeiro se o cadastro foi bem-sucedido

def obter_usuario_atual():
    """Retorna o nome do usuário atual."""
    # Retorna o nome do usuário que está logado no momento
    return _usuario_atual

def definir_usuario_atual(nome):
    """Define o usuário atual."""
    # Declara que vamos usar a variável global
    global _usuario_atual
    # Define qual usuário está logado no momento
    _usuario_atual = nome

# Variável global para armazenar o usuário logado
# Começa como None (nenhum usuário logado)
_usuario_atual = None