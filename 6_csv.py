import csv


# try:
#     with open("usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(["id", "nome"])
#         escritor.writerow(["1", "Maria"])
#         escritor.writerow(["2", "João"])
# except IOError as exc:
#     print(f"Erro ao criar o arquivo. {exc}")


# try:
#     with open("usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
#         leitor = csv.reader(arquivo)
#         for row in leitor:
#             print(row)
# except IOError as exc:
#     print(f"Erro ao criar o arquivo. {exc}")


try:
    with open("usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro ao criar arquivo. {exc}")