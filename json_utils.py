#Ler o JSON caso não exista o arquivo ele cria o arquivo json no diretório do arquivo
import json

def read_json(path_):
    data = []
    try:
        with open(path_, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        save_employee([], path_)
    return data

#Salva os dados no arquivo JSON
def save_employee(data_, path_):
    try:
        with open(path_, 'w', encoding='utf-8') as file:
            json.dump(data_, file, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f'Error ao salvar os dados {e}')
        return False