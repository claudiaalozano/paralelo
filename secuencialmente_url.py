# Description: Ejemplo de secuencialidad en Python
import random
from time import sleep

urls=["a.com", "b.com", "c.com", "d.com"]

def scrape(url):
    print("starting", url)
    duration= round(random.random(), 3)
    sleep(duration)
    print("done", url,"time taken: " ,duration, " seconds.")
    return url, duration
    


