arquivo = open("teste.txt", "w")

arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "Escrevendo", "\n", "um", "\n", "novo", "\n", "texto."])
arquivo.close()