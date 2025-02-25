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