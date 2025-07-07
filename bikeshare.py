#!/usr/bin/env python3
# coding: utf-8

import csv
import matplotlib.pyplot as plt
import zipfile
import os.path

csv_name = 'chicago.csv'
csv_zip_name = 'chicago.csv.zip'

is_csv = os.path.isfile(csv_name)
is_csv_zip_name = os.path.isfile(csv_zip_name)

if is_csv_zip_name and not is_csv:
    print("Descompactando CSV file...")
    with zipfile.ZipFile('./chicago.csv.zip', 'r') as zip_ref:
        zip_ref.extractall('./')

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")

# TAREFA 1
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
print("\n")
for data in data_list[1:20]:
    print(data)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")


# TAREFA 2


print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
print("\n")
for data in data_list[0:19]:
    print(data[6])


input("Aperte Enter para continuar...")


# TAREFA 3


def column_to_list(_data, _index):
    _column_list = []

    for d in _data:
        _column_list.append(d[_index])
    return _column_list


# Vamos checar com os gêneros se isso está funcionando para os primeiros 20
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(
    data_list,
    -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(
    data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and \
       column_to_list(data_list, -2)[1] == "Male",\
       "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 4


male = len(
    list(
        filter(lambda gender: gender == 'Male', column_to_list(data_list,
                                                               -2))))
female = len(
    list(
        filter(lambda gender: gender == 'Female', column_to_list(
            data_list, -2))))

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 5


def count_gender(_data_list):
    _male = len(
        list(
            filter(lambda gender: gender == 'Male',
                   column_to_list(_data_list, -2))))
    _female = len(
        list(
            filter(lambda gender: gender == 'Female',
                   column_to_list(_data_list, -2))))
    return [_male, _female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(
    count_gender(data_list)
) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(
    count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and \
       count_gender(data_list)[1] == 298784, \
       "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 6


def most_popular_gender(_data_list):
    _male, _female = count_gender(_data_list)
    _answer = ""
    if _male == _female:
        _answer = "Equal"
    elif _male > _female:
        _answer = "Male"
    else:
        _answer = "Female"
    return _answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(
    most_popular_gender(data_list)
) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(
    data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
# gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")


# TAREFA 7


print("\nTAREFA 7: Verifique o gráfico!")
user_types = set(column_to_list(data_list, -3))
user_types_dict = {}
for utype in user_types:
    length = len(
        list(
            filter(lambda user: user == utype, column_to_list(data_list, -3))))
    user_types_dict[utype] = length

print(user_types_dict)

types = list(user_types_dict.keys())
quantity = list(user_types_dict.values())
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantidade por User Type')
plt.show(block=True)

input("Aperte Enter para continuar...")


# TAREFA 8


male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque há vários registros em branco. " \
         "Então a soma correta seria: male + female + branco. "
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", \
    "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 9


# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
sorted_int_list = sorted(list(map(int, trip_duration_list)))
list_len = len(sorted_int_list)
index = (list_len - 1) // 2

min_trip = sorted_int_list[0]
max_trip = sorted_int_list[-1]
mean_trip = sum(sorted_int_list) / len(sorted_int_list)
median_trip = sorted_int_list[index] if list_len % 2 else (
    sorted_int_list[index] + sorted_int_list[index + 1]) / 2

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ",
      median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 10


start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(
    start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 11


def new_function(param1: int, param2: str) -> list:
    """
    Função de exemplo com anotações.
    Argumentos:
        param1: O primeiro parâmetro.
        param2: O segundo parâmetro.
    Retorna:
       Uma lista de valores x.
    """
    print(param1, param2)  # apenas para fins de PEP8
    return []  # apenas para fins de PEP8


input("Aperte Enter para continuar...")


# TAREFA 12


# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(_column_list):
    _data_types = set(_column_list)
    _data_types_dict = {}
    for _utype in _data_types:
        _length = len(list(filter(lambda user: user == _utype, _column_list)))
        _data_types_dict[_utype] = _length
    _item_types = user_types_dict.keys()
    _count_items = user_types_dict.values()
    return _item_types, _count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------