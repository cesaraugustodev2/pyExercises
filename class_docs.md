# Documentação da Classe Wallet

## Descrição

A classe `Wallet` representa uma carteira que pode armazenar um saldo e contar o número de reembolsos realizados.

## Atributos

- `refund_count` (int): Uma variável de classe para contar o número de reembolsos.
- `balance` (float): O saldo atual da carteira.

## Métodos

### `__init__()`

Inicializa a carteira com um saldo de 0.

### `add_funds(amount: float)`

Adiciona a quantia especificada ao saldo da carteira.

- **Parâmetros:**
  - `amount` (float): A quantia a ser adicionada ao saldo.

### `remove_funds(amount: float)`

Remove a quantia especificada do saldo da carteira, se houver fundos suficientes.

- **Parâmetros:**
  - `amount` (float): A quantia a ser removida do saldo.

- **Retorna:**
  - `bool`: `True` se a quantia foi removida com sucesso, `False` caso contrário.

### `get_balance()`

Retorna o saldo atual da carteira.

- **Retorna:**
  - `float`: O saldo atual da carteira.

### `add_refund()`

Incrementa o contador global de reembolsos.

### `check_refund()`

Imprime o contador global de reembolsos.

# Documentação da Classe Book

## Descrição

A classe `Book` representa um livro que pode ser vendido e reembolsado, e mantém um registro das transações em uma carteira associada.

## Atributos

- `title` (str): O título do livro.
- `author` (str): O autor do livro.
- `year` (int): O ano de publicação do livro.
- `price` (float): O preço do livro.
- `wallet` (Wallet): Uma instância da classe `Wallet` para registrar as transações.

## Métodos

### `__init__(title: str, author: str, year: int, price: float)`

Inicializa o livro com o título, autor, ano de publicação e preço especificados.

- **Parâmetros:**
  - `title` (str): O título do livro.
  - `author` (str): O autor do livro.
  - `year` (int): O ano de publicação do livro.
  - `price` (float): O preço do livro.

### `new_order(qty: int)`

Registra uma nova ordem de venda para o livro.

- **Parâmetros:**
  - `qty` (int): A quantidade de cópias vendidas.

### `check_wallet()`

Imprime o saldo atual da carteira associada ao livro.

### `refund()`

Processa um reembolso para o livro, removendo o valor do preço do livro da carteira e incrementando o contador de reembolsos.