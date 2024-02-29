import json

# Função para ler o arquivo JSON
def read_json(path_):
    data = []
    try:
        # Tenta abrir o arquivo JSON e carregar os dados
        with open(path_, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        # Se o arquivo não for encontrado, cria um novo arquivo JSON vazio
        save_employee([], path_)
    return data

# Função para salvar os dados no arquivo JSON
def save_employee(data_, path_):
    try:
        # Tenta abrir o arquivo JSON para escrita e salvar os dados
        with open(path_, 'w', encoding='utf-8') as file:
            # Salva os dados no arquivo com formatação e codificação adequadas
            json.dump(data_, file, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        # Em caso de erro, imprime a mensagem de erro
        print(f'Error ao salvar os dados {e}')
        return False