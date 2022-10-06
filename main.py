import requests
import time

while True:
    try:
        r = requests.get('https://supportxmr.com/api/miner/431C8VfymXv65xxuFFP1EcBFFf3aik6676okEjhpryC84bM4TxYbUVqN39Kkq62u3HXYr853EAMzbJQeuFTR5KygCPpdnXV/stats')
        j = r.json()
        print(j["hash"])
        f = open("data.txt", "a")
        f.write(r.text + "\n")
        f.close()
    except:
        print("Bla Fehler iwas...")
    time.sleep(3)
