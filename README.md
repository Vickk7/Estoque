# 🏪 Sistema de Controle de Estoque

Olá! 👋 Este é um sistema super legal para controlar o estoque de uma loja! Vamos aprender como ele funciona?

## 📦 O que este programa faz?

Este programa ajuda a:
- ✏️ Cadastrar produtos novos
- 📋 Listar todos os produtos
- ➕ Adicionar produtos ao estoque
- ➖ Retirar produtos do estoque
- 📊 Ver relatórios sobre o estoque

## 🎨 Como o programa é organizado?

O programa é dividido em várias partes, como peças de LEGO! Vamos ver cada uma:

### 📁 Estrutura de Pastas

```
app/
├── main.py           -> A porta de entrada do programa! 🚪
├── login_window.py   -> Tela para entrar no sistema 🔑
├── main_window.py    -> Tela principal do programa 🏠
├── stock_manager.py  -> Cuida dos produtos no estoque 📦
├── user_manager.py   -> Cuida dos usuários 👥
├── ui_helpers.py     -> Ajuda a fazer as telas bonitas ✨
└── view/            -> Todas as telas do programa 🖥️
    ├── product_registration.py -> Cadastro de produtos ✏️
    ├── product_listing.py     -> Lista de produtos 📋
    ├── stock_movement.py      -> Entrada e saída de produtos ↕️
    └── reports.py            -> Relatórios do estoque 📊

data/
├── usuarios.json    -> Guarda informações dos usuários 👥
├── estoque.json    -> Guarda informações dos produtos 📦
└── movimentos.json -> Guarda entrada e saída de produtos 📝
```

## 🚀 Como usar o programa?

### 1️⃣ Preparando tudo

Primeiro, você precisa ter:
- Python 3.11 ou mais novo instalado no computador
- As bibliotecas necessárias instaladas

Para instalar as bibliotecas, abra o terminal e digite:
```bash
pip install -r requirements.txt
```

### 2️⃣ Iniciando o programa

1. Abra o terminal
2. Vá até a pasta do programa
3. Digite:
```bash
python -m app.main
```

### 3️⃣ Usando o programa

1. **Login** 🔑
   - Digite seu nome de usuário e senha
   - Se não tiver uma conta, clique em "Cadastrar"

2. **Tela Principal** 🏠
   - No menu, escolha o que quer fazer
   - Cada botão leva para uma função diferente

3. **Cadastro de Produtos** ✏️
   - Clique em "Cadastro de Produtos"
   - Preencha todas as informações
   - Clique em "Salvar"

4. **Movimentação de Estoque** ↕️
   - Escolha "Entrada" para adicionar produtos
   - Escolha "Saída" para retirar produtos
   - Digite o código do produto
   - Digite a quantidade
   - Clique em "Confirmar"

5. **Relatórios** 📊
   - Veja quantos produtos tem no estoque
   - Acompanhe as entradas e saídas
   - Veja informações importantes sobre o estoque

## 📚 Exemplos Práticos

### 1️⃣ Cadastrando um Novo Produto

Vamos cadastrar um pacote de bolacha:
```
Código: 123
Nome: Bolacha Recheada
Descrição: Pacote de bolacha recheada sabor chocolate
Preço: 3.50
Quantidade: 50
Categoria: Biscoitos
```

Depois de salvar, o produto estará disponível para movimentação!

### 2️⃣ Fazendo uma Entrada no Estoque

Chegaram mais bolachas:
```
Código: 123
Quantidade: 30
Descrição: Recebimento de mercadoria
```

Agora temos 80 pacotes no estoque (50 + 30)!

### 3️⃣ Registrando uma Saída

Vendemos algumas bolachas:
```
Código: 123
Quantidade: 5
Descrição: Venda para cliente
```

Agora temos 75 pacotes no estoque (80 - 5)!

### 4️⃣ Consultando o Relatório

No relatório você pode ver:
```
Produto: Bolacha Recheada
Código: 123
Quantidade Atual: 75
Movimentações:
- ➕ Entrada: 50 (Cadastro inicial)
- ➕ Entrada: 30 (Recebimento de mercadoria)
- ➖ Saída: 5 (Venda para cliente)
```

### 5️⃣ Exemplos de Categorias

Algumas sugestões de categorias para organizar seus produtos:
- 🍪 Biscoitos
- 🥤 Bebidas
- 🧀 Laticínios
- 🥖 Padaria
- 🧻 Limpeza
- 📝 Papelaria

### 6️⃣ Dicas de Organização

Códigos de produtos podem seguir um padrão:
- 1XX: Alimentos
- 2XX: Bebidas
- 3XX: Limpeza
- 4XX: Papelaria

Exemplo:
```
101: Bolacha Recheada
102: Salgadinho
201: Refrigerante
202: Suco
301: Detergente
401: Caderno
```

## 🎯 Recursos Legais

- 🌈 Interface colorida e fácil de usar
- 🔍 Busca rápida de produtos
- 📱 Design moderno
- 🔒 Sistema seguro com login
- 📊 Relatórios completos
- ⚡ Respostas rápidas

## 🤝 Como Contribuir

Você pode ajudar a melhorar este programa! Aqui está como:
1. 🍴 Faça um fork do projeto
2. 🔧 Faça suas mudanças
3. 📫 Envie um pull request

## 📝 Arquivos Importantes

- `main.py`: Inicia o programa
- `login_window.py`: Cuida do login
- `stock_manager.py`: Gerencia o estoque
- `view/*.py`: Todas as telas do programa

## ⚙️ Configuração do Ambiente

1. Instale o Python 3.11 ou mais novo
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## ❓ Problemas Comuns e Soluções

### 1️⃣ "Não consigo fazer login"

**Problema**: Mensagem de erro ao tentar entrar no sistema.

**Soluções**:
1. Verifique se digitou o nome de usuário corretamente
2. Confira se a tecla Caps Lock está desligada
3. Se esqueceu a senha, crie uma nova conta

### 2️⃣ "O produto não aparece na lista"

**Problema**: Produto cadastrado não aparece na listagem.

**Soluções**:
1. Verifique se salvou o cadastro (deve aparecer mensagem de sucesso)
2. Tente limpar o filtro de busca
3. Confira se digitou o código corretamente
4. Clique no botão "Atualizar" da lista

### 3️⃣ "Não consigo dar saída no produto"

**Problema**: Erro ao tentar registrar saída de produtos.

**Soluções**:
1. Verifique se há quantidade suficiente em estoque
2. Confira se o código do produto está correto
3. A quantidade deve ser maior que zero
4. Certifique-se de estar na aba "Saída"

### 4️⃣ "Os relatórios estão vazios"

**Problema**: Relatórios não mostram informações.

**Soluções**:
1. Verifique se há produtos cadastrados
2. Selecione o tipo correto de relatório
3. Clique em "Gerar Relatório"
4. Confira se houve movimentações no período

### 5️⃣ "O programa não abre"

**Problema**: Erro ao iniciar o programa.

**Soluções**:
1. Verifique se o Python está instalado:
   ```bash
   python --version  # Deve mostrar versão 3.11 ou maior
   ```
2. Confira se instalou as dependências:
   ```bash
   pip list  # Deve mostrar customtkinter e outras bibliotecas
   ```
3. Certifique-se de estar no diretório correto:
   ```bash
   cd caminho/do/projeto
   ```
4. Tente reinstalar as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### 6️⃣ "Os arquivos de dados sumiram"

**Problema**: Arquivos da pasta `data/` não existem ou foram corrompidos.

**Soluções**:
1. Verifique se a pasta `data/` existe
2. Crie os arquivos se não existirem:
   ```json
   // data/usuarios.json
   {}
   
   // data/estoque.json
   {}
   
   // data/movimentos.json
   []
   ```
3. Restaure um backup se tiver
4. Inicie o programa novamente

## 🌟 Dicas Legais

- Sempre faça login antes de usar
- Mantenha o código do produto anotado
- Faça backups dos arquivos da pasta `data/`
- Atualize o programa regularmente

Divirta-se usando o Sistema de Controle de Estoque! 🎉