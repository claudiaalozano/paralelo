# paralelo
Mi dirección de Github es: https://github.com/claudiaalozano/paralelo.git

En esta tarea hemos comparado el multiprocesamiento con la programación secuencial, analizando unos urls.

El código empleado para multiprocesing:
```
from multiprocessing import Pool
import random
from time import sleep

urls=["a.com", "b.com", "c.com", "d.com"]

def scrape(url):
    print("starting", url)
    duration= round(random.random(), 3)
    sleep(duration)
    print("done", url,"time taken: " ,duration, " seconds.")
    return url, duration
  ```
    
El código para secueencial:
```
import random
from time import sleep

urls=["a.com", "b.com", "c.com", "d.com"]

def scrape(url):
    print("starting", url)
    duration= round(random.random(), 3)
    sleep(duration)
    print("done", url,"time taken: " ,duration, " seconds.")
    return url, duration
    
 ```
 
