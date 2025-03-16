# Este arquivo é responsável por importar e disponibilizar as funções das diferentes telas do sistema
# Ele facilita o acesso às funções da pasta view a partir de outros arquivos

# Importa as funções principais de cada módulo (arquivo) da pasta view
from .product_registration import mostrar_cadastro_produto  # Tela de cadastro de produtos
from .stock_movement import mostrar_movimentacao  # Tela de movimentação de estoque
from .reports import mostrar_relatorios  # Tela de relatórios e consultas

# Define quais funções estarão disponíveis quando alguém importar da pasta view
# Por exemplo: from app.view import mostrar_cadastro_produto
__all__ = [
    'mostrar_cadastro_produto',
    'mostrar_movimentacao',
    'mostrar_relatorios'
]