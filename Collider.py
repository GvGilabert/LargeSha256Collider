import hashlib
import random
import datetime
import threading
from multiprocessing import Process


def Log(text):
    file = open("log.csv","a")
    file.write(text+"\n")
    file.close()

def HashSomething (hashThis):
    
    toFindBytes = hashThis.encode()
    hlib = hashlib.sha256()
    hlib.update(toFindBytes)
    BytesData = hlib.digest()
    return BytesData

def SearchCollisionSingle(hash,start,finish,bytesTo,msg):
    hashTo=HashSomething(hash)
    t1 = datetime.datetime.now()
    collisions = []
    q = str(start)+","+str(finish)+","+str(finish-start)

    while start<finish:
        newHash = HashSomething(str(start))        
        if newHash[0]==hashTo[0] and newHash[1]==hashTo[1] and newHash[2]==hashTo[2] and newHash[3]==hashTo[3] and\
           newHash[4]==hashTo[4] and newHash[5]==hashTo[5] and newHash[6]==hashTo[6] and newHash[7]==hashTo[7] and\
           newHash[8]==hashTo[8] and newHash[9]==hashTo[9] and newHash[10]==hashTo[10] and newHash[11]==hashTo[11] and\
           newHash[12]==hashTo[12] and newHash[13]==hashTo[13] and newHash[14]==hashTo[14] and newHash[15]==hashTo[15] and\
           newHash[16]==hashTo[16] and newHash[17]==hashTo[17] and newHash[18]==hashTo[18] and newHash[19]==hashTo[19] and\
           newHash[20]==hashTo[20] and newHash[21]==hashTo[21] and newHash[22]==hashTo[22] and newHash[23]==hashTo[23] and\
           newHash[24]==hashTo[24] and newHash[25]==hashTo[25] and newHash[26]==hashTo[26] and newHash[27]==hashTo[27] and\
           newHash[28]==hashTo[28] and newHash[29]==hashTo[29] and newHash[30]==hashTo[30] and newHash[31]==hashTo[31]:
            collisions.append(start)
        start += 1
    
    t2 = datetime.datetime.now()
    r = t2-t1
    Log(msg+","+str(hash)+","+q+","+str(len(collisions))+","+str(collisions).replace(',',' / ')+","+str(bytesTo)+","+str(r))


def Threader(threads, tries, startAt, hashTo, bytesTo):
    oh=tries%threads
    tpt=tries//threads 
    s = startAt
    f = startAt + oh + tpt
    cont=0
    while threads>0:
       cont+=1
       a = threading.Thread(target=SearchCollisionSingle, args=(hashTo,s,f,bytesTo,"Thread "+str(cont)+"/"+str(threads+cont-1)+" No Join"))
       a.start()
       #a.join
       s = f+1
       f += tpt
       threads -= 1

def Processer(processes, tries, startAt, hashTo, bytesTo):
    oh=tries%processes
    tpt=tries//processes 
    s = startAt
    f = startAt + oh + tpt
    cont=0
    while processes>0:    
        cont+=1
        if __name__ == '__main__':
            p = Process(target=SearchCollisionSingle, args=(hashTo,s,f,bytesTo,"Process "+str(cont)+"/"+str(processes+cont-1)+" No Join"))
            p.start()
        #a.join
        s = f+1
        f += tpt
        processes -= 1

HASHTOFIND = "germangilabert"
TRIES =   1000000000
STARTAT = 176000000
BYTESTOCHECK = 32
THREADS = 8
PROCESSES = 8

#Threader(THREADS,TRIES,STARTAT,HASHTOFIND,BYTESTOCHECK)
Processer(THREADS,TRIES,STARTAT,HASHTOFIND,BYTESTOCHECK)
