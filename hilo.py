import threading

def worker(count):
    print("conteo " + str(count)+"\n")
    return
threads = list()
for i in range(3):
    t = threading.Thread(target=worker,args=(i,))
    threads.append(t)
    t.start()