## Validação de Classes de Carros em Python ##
Este repositório contém um exemplo de código Python que demonstra a criação de classes com Programação Orientada a Objetos (POO), focando em validação de dados e herança. O objetivo é criar objetos Carro com atributos específicos, garantindo que os dados inseridos sejam válidos, e mostrar como estender essa funcionalidade com classes filhas.

## Funcionalidades ##
A classe Carro oferece as seguintes funcionalidades e validações:

## Atributos: ##

name (str): Nome ou modelo do carro (ex: "Fox", "Cobalt").

brand (str): Marca do carro (ex: "Volkswagen", "Chevrolet").

color (str): Cor do carro (ex: "Red", "Black").

year (int): Ano de fabricação do carro.

is_new (bool): Indica se o carro é novo ou usado.

Validação de Ano: O ano de fabricação deve estar entre 1950 e 2025 (inclusive). Tentativas de criar um carro com ano fora desse intervalo resultarão em um ValueError.

Validação de Marca: A marca do carro deve ser uma das seguintes: "Chevrolet", "Volkswagen" ou "Mitsubishi". Qualquer outra marca resultará em um ValueError.

Método drive(): Um método simples que imprime uma mensagem indicando que o carro está sendo dirigido, exibindo seus principais atributos.

Herança: A classe SportsCar (Carro Esportivo) demonstra como herdar todas as funcionalidades e validações da classe Carro, podendo ser estendida para incluir características específicas de carros esportivos no futuro.
