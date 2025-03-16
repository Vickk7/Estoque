# Este arquivo controla a tela de relatórios do sistema
# Aqui estão as funções para mostrar informações do estoque e movimentações

# Importa bibliotecas para criar a interface gráfica
import customtkinter as ctk

# Importa funções auxiliares para criar elementos visuais
from app.ui_helpers import (
    criar_combobox,
    criar_botao,
    limpar_frame,
    criar_tabela
)

# Importa funções para obter os dados do estoque
from app.stock_manager import (
    listar_produtos,
    obter_movimentos,
    obter_produto
)

def mostrar_relatorios(frame_pai):
    """Exibe a tela de relatórios do estoque."""
    # Limpa qualquer conteúdo anterior da tela
    limpar_frame(frame_pai)
    
    # Adiciona o título da tela
    ctk.CTkLabel(
        frame_pai, 
        text="Relatórios", 
        font=("Arial", 20, "bold")
    ).pack(pady=20)
    
    # Cria um quadro para as opções de relatório
    frame_opcoes = ctk.CTkFrame(frame_pai)
    frame_opcoes.pack(pady=10, padx=20, fill="x")
    
    # Adiciona uma caixa de seleção (combobox) para escolher o tipo de relatório
    ctk.CTkLabel(frame_opcoes, text="Tipo de Relatório:").pack(side="left", padx=5)
    combo_relatorio = criar_combobox(
        frame_opcoes,
        valores=["Produtos em Estoque", "Movimentações"]
    )
    combo_relatorio.pack(side="left", padx=5)
    
    # Cria um quadro para mostrar os resultados do relatório
    frame_relatorio = ctk.CTkFrame(frame_pai)
    frame_relatorio.pack(pady=10, padx=20, fill="both", expand=True)
    
    # Cria uma tabela para mostrar os dados
    colunas = ("Código", "Nome", "Quantidade", "Categoria", "data")
    tabela, scrollbar = criar_tabela(frame_relatorio, colunas)
    tabela.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Função executada quando o botão Gerar Relatório é clicado
    def gerar_relatorio():
        # Obtém o tipo de relatório selecionado
        tipo_relatorio = combo_relatorio.get()
        # Limpa os dados antigos da tabela
        for item in tabela.get_children():
            tabela.delete(item)
        
        # Gera o relatório conforme o tipo selecionado
        if tipo_relatorio == "Produtos em Estoque":
            # Obtém a lista de produtos do estoque
            produtos = listar_produtos()
            # Adiciona cada produto à tabela
            for codigo, produto in produtos:
                tabela.insert("", "end", values=(
                    codigo,
                    produto["nome"],
                    produto["quantidade"],
                    produto["categoria"],
                    produto["data_cadastro"]
                ))
        elif tipo_relatorio == "Movimentações":
            # Obtém o histórico de movimentações do estoque
            movimentos = obter_movimentos()
            # Adiciona cada movimento à tabela
            for mov in movimentos:
                # Obtém o nome do produto a partir do código
                produto = obter_produto(mov["codigo"])
                nome_produto = produto["nome"] if produto else "Produto não encontrado"
                # Insere uma linha na tabela
                tabela.insert("", "end", values=(
                    mov["codigo"],
                    nome_produto,
                    mov["quantidade"],
                    mov["tipo"],
                    mov["data"]
                ))
    
    # Adiciona o botão para gerar o relatório
    botao_gerar = criar_botao(frame_opcoes, "Gerar Relatório", gerar_relatorio)
    botao_gerar.pack(side="left", padx=5)
    
    # Gera um relatório inicial quando a tela é aberta
    gerar_relatorio()