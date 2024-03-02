import re

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
            yield f"{archivo}\t{x.group()}"
        else:
            yield None
           
            

