# Este arquivo contém todas as funções para gerenciar o estoque de produtos
# Aqui estão as operações como cadastrar, remover, atualizar e consultar produtos

# Importa bibliotecas para trabalhar com arquivos e datas
import json
import os
import datetime

# Função que garante que a pasta de dados existe
def garantir_diretorio():
    # Verifica se a pasta "data" existe e a cria se não existir
    if not os.path.exists("data"):
        os.makedirs("data")

# Define os caminhos dos arquivos onde os dados serão salvos
ARQUIVO_ESTOQUE = "./data/estoque.json"  # Armazena informações dos produtos
ARQUIVO_MOVIMENTOS = "./data/movimentos.json"  # Armazena histórico de movimentações

def carregar_estoque():
    """Carrega os dados do estoque do arquivo JSON."""
    # Garante que a pasta data existe
    garantir_diretorio()
    # Verifica se o arquivo de estoque existe
    if not os.path.exists(ARQUIVO_ESTOQUE):
        return {}  # Retorna um dicionário vazio se o arquivo não existir
    try:
        # Abre o arquivo e carrega seu conteúdo
        with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Se houver erro ao ler o arquivo, retorna um dicionário vazio
        return {}

def salvar_estoque(dados):
    """Salva os dados do estoque no arquivo JSON."""
    # Garante que a pasta data existe
    garantir_diretorio()
    # Salva os dados no arquivo
    with open(ARQUIVO_ESTOQUE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

def carregar_movimentos():
    """Carrega o histórico de movimentos do estoque."""
    # Garante que a pasta data existe
    garantir_diretorio()
    # Verifica se o arquivo de movimentos existe
    if not os.path.exists(ARQUIVO_MOVIMENTOS):
        return []  # Retorna uma lista vazia se o arquivo não existir
    try:
        # Abre o arquivo e carrega seu conteúdo
        with open(ARQUIVO_MOVIMENTOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Se houver erro ao ler o arquivo, retorna uma lista vazia
        return []

def salvar_movimentos(dados):
    """Salva o histórico de movimentos do estoque."""
    # Garante que a pasta data existe
    garantir_diretorio()
    # Salva os dados no arquivo
    with open(ARQUIVO_MOVIMENTOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

def adicionar_produto(codigo, nome, preco, quantidade, categoria):
    """Adiciona um novo produto ao estoque ou atualiza se já existir."""
    # Carrega os dados atuais do estoque
    estoque = carregar_estoque()
    
    # Cria um dicionário com as informações do produto
    produto = {
        "nome": nome,
        "preco": float(preco),  # Converte o preço para número decimal
        "quantidade": int(quantidade),  # Converte a quantidade para número inteiro
        "categoria": categoria,
        "data_cadastro": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Data e hora atual
    }
    
    # Adiciona ou atualiza o produto no estoque usando o código como chave
    estoque[codigo] = produto
    # Salva as alterações no arquivo
    salvar_estoque(estoque)
    
    # Registra a operação no histórico de movimentos
    registrar_movimento("Cadastro", codigo, quantidade, f"Cadastro do produto {nome}")
    return True

def remover_produto(codigo):
    """Remove um produto do estoque."""
    # Carrega os dados atuais do estoque
    estoque = carregar_estoque()
    # Verifica se o produto existe
    if codigo not in estoque:
        return False  # Retorna falso se o produto não existir
    
    # Guarda o nome do produto antes de removê-lo
    nome = estoque[codigo]["nome"]
    # Remove o produto do estoque
    del estoque[codigo]
    # Salva as alterações no arquivo
    salvar_estoque(estoque)
    
    # Registra a operação no histórico de movimentos
    registrar_movimento("Remoção", codigo, 0, f"Produto {nome} removido do estoque")
    return True

def atualizar_quantidade(codigo, quantidade, tipo_movimento):
    """Atualiza a quantidade de um produto no estoque."""
    # Carrega os dados atuais do estoque
    estoque = carregar_estoque()
    # Verifica se o produto existe
    if codigo not in estoque:
        return False  # Retorna falso se o produto não existir
    
    # Converte a quantidade para número inteiro
    quantidade = int(quantidade)
    # Obtém as informações do produto
    produto = estoque[codigo]
    nome = produto["nome"]
    
    # Verifica o tipo de movimento (entrada ou saída)
    if tipo_movimento == "entrada":
        # Adiciona a quantidade ao estoque atual
        produto["quantidade"] += quantidade
        movimento = "Entrada"
        mensagem = f"Entrada de {quantidade} unidades de {nome}"
    else:  # saída
        # Verifica se há estoque suficiente para a saída
        if produto["quantidade"] < quantidade:
            return False  # Retorna falso se não houver estoque suficiente
        # Subtrai a quantidade do estoque atual
        produto["quantidade"] -= quantidade
        movimento = "Saída"
        mensagem = f"Saída de {quantidade} unidades de {nome}"
    
    # Salva as alterações no arquivo
    salvar_estoque(estoque)
    # Registra a operação no histórico de movimentos
    registrar_movimento(movimento, codigo, quantidade, mensagem)
    return True

def registrar_movimento(tipo, codigo, quantidade, descricao):
    """Registra um movimento no histórico."""
    # Carrega o histórico atual de movimentos
    movimentos = carregar_movimentos()
    
    # Cria um dicionário com as informações do movimento
    movimento = {
        "data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Data e hora atual
        "tipo": tipo,
        "codigo": codigo,
        "quantidade": quantidade
    }
    
    # Adiciona o movimento ao histórico
    movimentos.append(movimento)
    # Salva as alterações no arquivo
    salvar_movimentos(movimentos)

def listar_produtos(filtro=None, valor=None):
    """Lista produtos com opção de filtro."""
    # Carrega os dados atuais do estoque
    estoque = carregar_estoque()
    
    # Se não houver filtro, retorna todos os produtos
    if not filtro or not valor:
        return list(estoque.items())
    
    # Se houver filtro, procura os produtos que correspondem ao critério
    resultado = []
    for codigo, produto in estoque.items():
        # Filtra por código do produto
        if filtro == "codigo" and codigo.lower().find(valor.lower()) >= 0:
            resultado.append((codigo, produto))
        # Filtra por nome do produto
        elif filtro == "nome" and produto["nome"].lower().find(valor.lower()) >= 0:
            resultado.append((codigo, produto))
        # Filtra por categoria do produto
        elif filtro == "categoria" and produto["categoria"].lower() == valor.lower():
            resultado.append((codigo, produto))
    
    return resultado

def obter_produto(codigo):
    """Retorna um produto específico pelo código."""
    # Carrega os dados atuais do estoque
    estoque = carregar_estoque()
    # Retorna o produto se existir, ou None se não existir
    return estoque.get(codigo)

def obter_categorias():
    """Retorna todas as categorias cadastradas."""
    # Carrega os dados atuais do estoque
    estoque = carregar_estoque()
    # Cria um conjunto (set) para armazenar as categorias sem repetição
    categorias = set()
    
    # Percorre todos os produtos e adiciona suas categorias ao conjunto
    for produto in estoque.values():
        categorias.add(produto["categoria"])
    
    # Converte o conjunto para lista e ordena alfabeticamente
    return sorted(list(categorias))

def obter_movimentos(filtro=None, valor=None):
    """Retorna o histórico de movimentos, com opção de filtro."""
    # Carrega o histórico atual de movimentos
    movimentos = carregar_movimentos()
    
    # Se não houver filtro, retorna todos os movimentos
    if not filtro or not valor:
        return movimentos
    
    # Se houver filtro, procura os movimentos que correspondem ao critério
    resultado = []
    for movimento in movimentos:
        # Filtra por tipo de movimento (entrada, saída, cadastro, remoção)
        if filtro == "tipo" and movimento["tipo"].lower() == valor.lower():
            resultado.append(movimento)
        # Filtra por código do produto
        elif filtro == "codigo" and movimento["codigo"].lower().find(valor.lower()) >= 0:
            resultado.append(movimento)
        # Filtra por data do movimento
        elif filtro == "data" and movimento["data"].startswith(valor):
            resultado.append(movimento)
    
    return resultado