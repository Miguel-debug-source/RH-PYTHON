# Sistema de Cadastro de Funcionários

Um sistema simples de cadastro de funcionários em Python que armazena os dados em um arquivo JSON.

## Instruções de Uso

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado em seu sistema.
3. Execute o arquivo main.py para iniciar o programa.
4. Siga as instruções apresentadas no console para adicionar, listar, buscar ou remover funcionários.

## Estrutura do Projeto

- `main.py`: Arquivo principal que contém a lógica do programa.
- `json_utils.py`: Módulo contendo funções para ler e salvar dados em formato JSON.
- `employees.json`: Arquivo JSON para armazenar os dados dos funcionários. Este arquivo é criado automaticamente se não existir quando o programa é executado.

## Documentação das Funções

- `read_json(path_)`: Função para ler os dados do arquivo JSON. Se o arquivo não existir, um novo arquivo vazio é criado.
- `save_employee(data_, path_)`: Função para salvar os dados no arquivo JSON.

## Exemplos de Uso

Para adicionar um novo funcionário, execute o programa e escolha a opção correspondente no menu.

Para listar todos os funcionários cadastrados, execute o programa e escolha a opção correspondente no menu.

...

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações de recebimento.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
