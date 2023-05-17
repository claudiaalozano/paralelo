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

if __name__ == "__main__":
    pool= Pool(processes=4)
    data= pool.map(scrape, urls)

    pool.close()

    for row in data:
        print(row)
