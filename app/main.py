# Este é o arquivo principal do programa, que inicia toda a aplicação
# Quando alguém executa este arquivo, o sistema de controle de estoque é iniciado

# Esta linha importa a função que vai mostrar a tela de login
from app.login_window import iniciar_login

# Esta parte verifica se o arquivo está sendo executado diretamente
# Se sim, inicia a tela de login para que o usuário possa entrar no sistema
if __name__ == "__main__":
    iniciar_login()
