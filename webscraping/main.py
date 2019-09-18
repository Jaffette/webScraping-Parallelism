import os
from time import time

def main():
    tiempo_inicial = time() 
    os.system("scrapy crawl gdp -o gdp.json")
    os.system("scrapy crawl mobile -o mobile.json")
    os.system("scrapy crawl internet -o internet.json")
    tiempo_final = time() 
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print ('El tiempo de ejecucion fue:',tiempo_ejecucion)

main()
