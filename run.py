from multiprocesamiento_url import *
from secuencialmente_url import *

if __name__ == "__main__":
    a=int(input("Ingrese 1 para secuencialmente_url.py o 2 para multiprocesamiento_url.py: "))
    if a==1:
        output= []
        for url in urls:
            result= scrape(url)
            output.append(result)
            
    elif a==2:
        pool= Pool(processes=4)
        data= pool.map(scrape, urls)

        pool.close()

        for row in data:
            print(row)


    