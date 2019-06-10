import hashlib
import random
import datetime
import threading

class HashedItem:
    BytesData=""
    HexData=""


def HashSomething (hashThis):
    h = HashedItem()
    toFindBytes = hashThis.encode()
    hlib = hashlib.sha256()
    hlib.update(toFindBytes)
    h.BytesData = hlib.digest()
    h.HexData = hlib.hexdigest()
    return h


def SearchCollision (hash,start,finish,collisions):
    threadName="Thread from "+str(start)+" to "+str(finish) 
    time = datetime.datetime.now()
    col = 0
    while start<finish:
        start += 1
        newHash = HashSomething(str(start)).BytesData
        matchs=0
        print(start)

        for i in range(BYTESTOCHECK):
            if(newHash[i]==hash[i]):
                matchs += 1
        if(matchs == BYTESTOCHECK):
            collisions.append(start)
            col = col+1
    print (threadName)
    print("Encontradas",col,"colisiones","demorando",datetime.datetime.now()-time)    
    


HASHTOFIND = "german gilabert"
TRIES = 100000
STARTAT = 983012387
BYTESTOCHECK = 1
THREADS = 4

totalCollisions = []
triesPerThread = TRIES // THREADS
f=STARTAT
t=STARTAT + triesPerThread
hashBytes = HashSomething(HASHTOFIND).BytesData


while THREADS>0:
    a = threading.Thread(target=SearchCollision, args=(hashBytes,f,t,totalCollisions))
    a.start()
    f += triesPerThread
    t += triesPerThread
    THREADS -=1

print("Para el hash", HashSomething(HASHTOFIND).HexData)


