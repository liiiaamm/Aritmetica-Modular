"""
imatlab.py

Matemática Discreta - IMAT
ICAI, Universidad Pontificia Comillas

Grupo: GPxxx
Integrantes:
    - XX
    - XX

Descripción:
Sistema interactivo IMAT-LAB de resolución de ecuaciones en aritmética modular.

Interfaz de acceso interactivo o por lotes a la librería modular.py. Si este script se ejecuta sin par´ametros,
lanzar´a la interfaz de usuario para el modo interactivo.
"""

from typing import TextIO
import modular 
import sys


""" Recibe un manejador fin de un fichero de texto ya abierto para lectura y otro de un fichero de salida
ya abierto para escritura y ejecuta línea por línea los comandos proporcionados por fin, escribiendo los resultados en fout. Si
fin y fout no corresponden con la entrada y salida esáandar, esta función ejecuta el modo de procesamiento
por lotes de IMAT-LAB para la entrada fin, guardando el resultado en el fichero fout.

    Args:
        fin (TextIO): Fichero de entrada. Manejador de un fichero de texto ya abierto para lectura.
        fout (TextIO): Fichero de salida. Manejador de un fichero de texto ya abierto para escritura.
    
    Returns: None
    
    Raises: None
    
    Examples:
        run_commands(sys.stdin,sys.stdout) lanza el modo interactivo y ejecuta línea por línea los comandos que
            el usuario lanza desde la entrada estándar.
"""

def run_commands(fin:TextIO,fout:TextIO):  #Para el modo por lotes
    comands_list = ["primo", "primos", "factorizar", "mcd", "coprimos", "pow", "inv", "euler", "legendre", "resolverSistema", "raiz", "ecCuadratica"]
    lines = fin.readlines()
    for line in lines:
        
        command, data = line.split("(")
        data = data.replace(")"," ").replace("\n", "")
        if command == "primo" and len(command) == 5:
            fout.write(str(modular.es_primo(int(data)))+"/n")


    
            

    

if __name__ == "__main__":
    pass

def separate_command(command:str):
    
    pass

def process_command(command:str, args:list):
    if command == "primo":
        a = int(args)
        return modular.es_primo(a)
    if command == "primos":
        a,b = int(args)
        return modular.lista_primos(a,b)
    if command == "factorizar":
        a = int(args)
        return modular.factorizar(a)
    if command == "mcd":
        a,b = int(args)
        return modular.mcd(a,b)   #También va aqui bezout
    if command == "coprimos":
        a,b = int(args)
        return modular.coprimos(a, b)
    if command == "pow":
        a,b,c = int(args)
        return modular.potencia_mod_p(a,b,c)
    if command == "inv":
        a,b = int(args)
        return modular.inversa_mod_p(a,b)
    if command == "euler":
        a,b = int(args)
        return modular.euler(a)
    if command == "legendre":
        a,b = int(args)
        return modular.legendre(a,b)
    if command == "resolverSistema":
        a,b = int(args) #adaptar a listas
        return modular.resolver_sistema_congruencias#rellenar#)
    if command == "raiz":
        a,b = int(args)
        return modular.raiz_mod_p(a,b)
    if command == "ecCuadratica":
        a,b,c,p = int(args)
        return modular.ecuacion_cuadratica(a,b,c,p)

def interactive_mode():
    while True:
        print("****Menú de operaciones****")
        line = sys.stdin.readline().strip()
        command, args = separate_command(line)
        print(process_command(command,args))



print("Desea entrar en modo interactivo? si/no")
line = sys.stdin.readline().strip()
if line.lower() == "si":
    interactive_mode()
else: 
    run_commands()
