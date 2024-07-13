try:
    with open("1lorem.txt", "r") as arquivo:
        print("Trabalhando com o arquivo")
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")


# try:
#     with open("arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")

try:
    with open("arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
except UnicodeDecodeError as exc:
    print(exc)