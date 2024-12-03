

def imprimirFichero(path):
    fich = open(path, 'r')
    for linea in fich:
        print(linea.rstrip())
    fich.close()
    


imprimirFichero("yob2005.txt")