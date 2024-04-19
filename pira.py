from pythonds.basic import Queue

def Pelanggan(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(Pelanggan(["Fatma","Karl","Toni","Asyraf","Barbie","Anjai", "Yani"],7))