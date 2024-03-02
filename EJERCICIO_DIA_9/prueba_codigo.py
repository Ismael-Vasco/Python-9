import re

ruta = "C:\\PYTHON_TOTAL\\archivo1.txt", "C:\\PYTHON_TOTAL\\archivo1.txt", "C:\\PYTHON_TOTAL\\archivo16.txt"
#texto = open(ruta, "r")
#patron = r"N\D{3}-\d{5}"
#x = re.search(patron,texto.read())
# - patron2 = "vestibulum"
#print(texto.read())
# - x = re.search(patron2, texto.read())
#print(x.group())
#print(f"{x}")
def leer_txt(txt):
     texto = open(txt, "r")
     return texto.read()

def buscador_de_similitudes(archivo):
    texto = leer_txt(archivo)
    #[N] + [tres carateres de texto] + [-] + [5 números]
    patron = r"N\D{3}-\d{5}"
    
    x = re.search(patron,texto)
    
    while True:

        if x:
            yield f"\t{archivo}\t\t{x.group()}"
        else:
            yield None

count = 0

for doc in ruta:  
    count +=1  

    arch = buscador_de_similitudes(doc)
    if next(arch) != None:
        print(next(arch))

print(count)