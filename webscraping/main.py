import os
from time import time
import threading
import json
import matplotlib.pyplot as plt
import numpy as np
def main():
    tiempo_inicial = time() 
    gdp()
    mobile()
    internet()
    tiempo_final = time() 
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    
    tiempo_inicial_thread = time()
    t1 = threading.Thread(target=gdp, args=())
    t2 = threading.Thread(target=mobile, args=())
    t3 = threading.Thread(target=internet, args=())

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    tiempo_final_thread = time()
    tiempo_ejecucion_thread = tiempo_final_thread - tiempo_inicial_thread
    #print ('El tiempo de ejecucion lineal fue:',tiempo_ejecucion)
    print ('El tiempo de ejecucion con thread fue fue:',tiempo_ejecucion_thread) 
    
    create_graphics()
    

def gdp():
    os.system("scrapy crawl gdp -o gdp.json")

def mobile():
    os.system("scrapy crawl mobile -o mobile.json")

def internet():
    os.system("scrapy crawl internet -o internet.json")
    
def get_gdp_json(): #This method get the gdp Json
    with open('gdp.json', 'r') as f:
        gdpJson = json.load(f)
        gpJsonSorted = sorted(gdpJson, key=lambda t:t['gdp'])
    return gpJsonSorted

def get_gdp_info(): # this method return 4 lists, two for the first 10 and the other for the last ones
    gdp = get_gdp_json()
    last_ten_num = []
    last_ten_name = []
    first_ten_num = []
    first_ten_name = []
    i = 0
    while i < 10:
        last_ten_num.append(gdp[i]['gdp'])
        last_ten_name.append(gdp[i]['name'])
        i += 1 

    j = len(gdp) -1
    while j >= len(gdp)-10:
        first_ten_num.append(gdp[j]['gdp'])
        first_ten_name.append(gdp[j]['name'])
        j -= 1 

    return last_ten_num, last_ten_name,first_ten_num,first_ten_name

def get_internet_json(): #This method get the internet Json
    with open('internet.json', 'r') as f:
        internetJson = json.load(f)
        netJsonSorted = sorted(internetJson, key=lambda t:t['internet'])
    return netJsonSorted

def get_internet_info(): # this method return 4 lists, two for the first 10 and the other for the last ones
    internet = get_internet_json()
    last_ten_num = []
    last_ten_name = []
    first_ten_num = []
    first_ten_name = []
    i = 0
    while i < 10:
        last_ten_num.append(internet[i]['internet'])
        last_ten_name.append(internet[i]['name'])
        i += 1 

    j = len(internet) -1
    while j >= len(internet)-10:
        first_ten_num.append(internet[j]['internet'])
        first_ten_name.append(internet[j]['name'])
        j -= 1 

    return last_ten_num, last_ten_name,first_ten_num,first_ten_name

def get_mobile_json(): #This method get the mobile Json
    with open('mobile.json', 'r') as f:
        mobileJson = json.load(f)
        mobJsonSorted = sorted(mobileJson, key=lambda t:t['mobile'])
    return mobJsonSorted
def get_mobile_info(): # this method return 4 lists, two for the first 10 and the other for the last ones
    mobile = get_mobile_json()
    last_ten_num = []
    last_ten_name = []
    first_ten_num = []
    first_ten_name = []
    i = 0
    while i < 10:
        last_ten_num.append(mobile[i]['mobile'])
        last_ten_name.append(mobile[i]['name'])
        i += 1 

    j = len(mobile) -1
    while j >= len(mobile)-10:
        first_ten_num.append(mobile[j]['mobile'])
        first_ten_name.append(mobile[j]['name'])
        j -= 1 

    return last_ten_num, last_ten_name,first_ten_num,first_ten_name

def create_graphics():
    last_gdp_num,last_gdp_name, first_gdp_num, first_gdp_name = get_gdp_info()
    last_internet_num,last_internet_name, first_internet_num, first_internet_name = get_internet_info()
    last_mobile_num,last_mobile_name, first_mobile_num, first_mobile_name = get_mobile_info()
    # GDP Fist 10
    plt.figure(figsize=(25,25))
    plt.subplot(321) 
    explode = [0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2] 
    plt.pie(first_gdp_num, labels = first_gdp_name,autopct='%1.1f%%', explode = explode, shadow=True)
    plt.title('Countries with highest GDP', bbox={"facecolor":"0.9", "pad":2})
    # GDP last 10
    plt.subplot(322)
    explode = [0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0, 0.1] 
    plt.pie(last_gdp_num, labels = last_gdp_name,autopct='%1.1f%%', explode = explode, shadow=True)
    plt.title('Countries with lowest GDP',bbox={"facecolor":"0.9", "pad":2})
    # internet fist 10
    plt.subplot(323)
    explode = [0, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2] 
    plt.pie(first_internet_num, labels = first_internet_name, autopct='%1.1f%%', explode = explode, shadow=True)
    plt.title('Countries with highest internet conections',bbox={"facecolor":"0.9", "pad":2})
    # internet last 10
    plt.subplot(324)
    explode = [0.3, 0.3, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0.1] 
    plt.pie(last_internet_num, labels = last_internet_name, autopct='%1.1f%%', explode = explode, shadow=True)
    plt.title('Countries with lowest internet conections',bbox={"facecolor":"0.9", "pad":2})
    # internet first 10
    plt.subplot(325)
    explode = [0, 0, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2] 
    plt.pie(first_mobile_num, labels = first_mobile_name, autopct='%1.1f%%',explode = explode, shadow=True)
    plt.title('Countries with highest mobile conections',bbox={"facecolor":"0.9", "pad":2})
    # internet last 10
    plt.subplot(326)
    explode = [0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0] 
    plt.pie(last_mobile_num, labels = last_mobile_name,autopct='%1.1f%%', explode = explode, shadow=True)
    plt.title('Countries with lowest mobile conections',bbox={"facecolor":"0.9", "pad":2})
    
    plt.show()
main()



