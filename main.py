import os
from json_utils import read_json, save_employee

# Caminho para o arquivo JSON
PATH_ = os.path.join(os.path.dirname(__file__), 'employees.json')

# Lista de opções do menu
OPTIONS = ['Adicionar Funcionarios ➕', 'Listar Functionarios 📋', 'Buscar Funcionarios 🔍', 'Remover Funcionários 🗑️', 'Sair Do programa 🛑']

# Função para adicionar um funcionário
def add_employee():
    # Solicita informações do usuário
    add_name = input('Informe o nome usuario que deseja adicionar: ').strip()
    # Validação do nome
    if not add_name:
        print('O Nome do Funcionário não pode ser vazio ⚠️ \n')
        return
    
    add_position = input('Informe o nome do cargo: ').strip()
    # Validação do cargo
    if not add_position:
        print('O cargo não pode ser vazio')
        return
    
    add_salary = input('Informe o salario do cargo: ')
    # Validação do salário
    try:
        conv_salary = float(add_salary)
    except ValueError:
        print('O Salário deve ser um número ⚠️\n')
        return
    if conv_salary <= 0:
        print('O Salário deve ser maior que zero ⚠️\n')
        return

    # Criação do dicionário de dados
    data_dic = {
        'nome' : add_name,
        'cargo' : add_position,
        'salário' : add_salary,
    }

    # Salva os dados
    employeeData.append(data_dic)
    if(save_employee(employeeData, PATH_)):
        print('\nUsuario cadastrado com sucesso ✅\n')
    else:
        print('\nError ao cadastrar o Funcionário 🛑\n')

# Função para listar os funcionários
def list_employee(data_):
    print(f'\nTotal de Funcionário: {len(data_)}')
    if not data_:
        print('Nenhum Funcionário Cadastrado\n')
        return

    for i, employee in enumerate(data_):
        print(f'{i+1}) Nome: {employee['nome']} | Cargo: {employee['cargo']} | Salário: {employee['salário']}')
    print()

# Função para pesquisar um funcionário    
def search_employee(data_):
    search_user_ = input('Informe o Nome do funcionário que deseja pesquisar: ').lower().strip()
    matches = [employee for employee in data_ if search_user_ in employee["nome"].lower().strip() ]
    
    if not matches:
        print('Funcionário não encontrado ⚠️')
        return

    for i in matches:
        print(f'Nome: {i['nome']} | Cargo: {i['cargo']}')

    print()

# Função para remover um funcionário
def remove_employee():
    if not employeeData:
        print('Nenhum Funcionário Cadastrado⚠️\n')
        return

    try:
        delete_employee = int(input('Informe o indice do usuário que deseja deletar: '))
        employeeData.pop(delete_employee - 1)
        if(save_employee(employeeData, PATH_)):
            print('\nUsuário removido com sucesso ✅\n')
        else:
            print('\nError ao remover o Funcionário 🛑\n')
    except IndexError:
        print('Usuario não encontrado ⚠️')
    except ValueError:
        print('A Entrada deve ser um número inteiro ⚠️')

# Lê os dados dos funcionários do arquivo JSON
employeeData = read_json(PATH_)

# Loop principal do programa
while True:
    # Exibe as opções do menu
    for number, op in enumerate(OPTIONS):
        print(f'({number}) {op}')

    # Solicita a escolha do usuário
    user_choice = input('Informe a ação que deseja realizar: ')
    if user_choice == '4': break

     # Dicionário de comandos para executar a ação escolhida
    commands = {
        '0': lambda: add_employee(),
        '1': lambda: list_employee(employeeData),
        '2': lambda: search_employee(employeeData),
        '3': lambda: remove_employee(),
    }

    # Executa o comando correspondente à escolha do usuário
    if commands.get(user_choice) is not None:
        command = commands.get(user_choice) 
        command()
    else:
        print ('\nComando não encontrado\n') 
        continue 

    



