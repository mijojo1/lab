#!/usr/bin/env python

import sys
import os
import zipfile
import argparse
from tqdm import tqdm
from threading import Thread
def unzip_archivo(archivo, password):
    try:
        zip = zipfile.ZipFile(archivo)
        zip.extractall(path=os.path.join(archivo[:-4]), pwd=str.encode(password))
        print("La clave del ZIP es :{}".format(password))
        #podemos variar el valor de -4,-10, depende si quieremos el Zip extraido en su totalidad
    except:
        pass
def main():
        #procesando la lista de posibles claves
    parser = argparse.ArgumentParser(
        usage="%(prog)s --zipfile <archivo zip> --test_passwords <lista de posibles claves>",
        description="Busca las palabras y combinaciones del diccionario de claves")
        #argumentos del Zip
    parser.add_argument("--zipfile",
                        dest="zipfile",
        #nombre del archivo zip a buscar su clave
                        default="maeforsai.zip")
        #argumentos de la lista de claves
    parser.add_argument("--test_passwords",
                        dest="test_passwords",
        #nombre de la lista del diccionario de claves
                        default="listaclaves.txt")
    options = parser.parse_args()
    with open(options.test_passwords) as dictionary_file:
        #tqdm ejecuta un ciclo para medir el progreso de la busqueda de claves
        for possible_password in tqdm(dictionary_file.readlines()):
            password = possible_password.strip()
            t = Thread(target=unzip_archivo, args=(options.zipfile, password))
            t.start()
if __name__ == "__main__":
    main()
