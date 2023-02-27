
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

pool= Pool(processes=4)

data= pool.map(scrape, urls)
scrape("a.com")
scrape("b.com")
scrape("c.com")
scrape("d.com")

pool.close()
print()
for row in data:
    print(data)
    