import tqdm as tq
import time as t
import sys
import os
from multiprocessing import Process as p
from queue import Queue as qu

ret = {'mul': 0.0, 'div': 0.0, 'add': 0.0, 'sub': 0.0}

# this was for thinking on splitting each process. this would of caused too many processes running at once for the processor.
# instead each operation list has its own process and then is timed for how long each process will take and how long it took to execute all of the processes
# def split(masterdata, lineslength, totalsplit):
#     splitlength = lineslength/totalsplit
#     returnlist = []
#     for i in range(int(splitlength)):
#         returnlist.append(masterdata.pop(0))
#     return returnlist

def main(totaliteration):
    # where the benchmark happens
    # just get some floating point operations in here to compute
    # thinking a text file import of datapoints and just multiply them over and over and then time it
    print('Loading Line Length...')
    f = open('data/data.csv', 'r')
    lineslength = len(f.readlines())
    #print(lineslength)
    f.close()

    f = open('data/data.csv', 'r')
    mydatamaster = []

    for i in tq.tqdm(range(lineslength), desc="Loading Lines…", ascii=False, ncols=100):
        myline = f.readline()
        leftdata, rightdata = myline.split(',')
        rightdata, dummydata = rightdata.split('\n')
        mydatamaster.append([leftdata, rightdata])

    f.close()
    f = open('data/results.csv', 'w')

    # this is for future speed up
    # splitlists = []
    # for i in range(PNUMBER):
    #     splitlists.append(split(mydatamaster, lineslength, PNUMBER))
    
    # print(len(splitlists.copy()))

    f.write('Total Number of Lines,' + str(lineslength) + '\n')
    for i in tq.tqdm(range(totaliteration), desc="Running Benchmarks…", ascii=False, ncols=100):

        # 9/7 this needs to be split amonst cores of the machine to get it to run faster.
        # i am farmiliar with threading so i would start there but multi process would work better for actual processor speed
        # basied off preliminary resarch, multiproccessing is written the same way as threading.

        # split into PNUMBER lists

        # p(target=mul,args=(splitlists.copy().pop(0), len(splitlists.copy().pop(0))))
        q = qu.Queue()
        q.put(ret)
        start_time = t.time()
        mulp = p(target=mul, args=(mydatamaster.copy(), lineslength, q))
        divp = p(target=div, args=(mydatamaster.copy(), lineslength, q))
        addp = p(target=add, args=(mydatamaster.copy(), lineslength, q))
        subp = p(target=sub, args=(mydatamaster.copy(), lineslength, q))
        mulp.start();divp.start();addp.start();subp.start()
        mulp.join();divp.join();addp.join();subp.join()
        results = q.get()
        total_time = t.time() - start_time
        multime = results['mul']
        divtime = results['div']
        addtime = results['add']
        subtime = results['sub']

        # multime = mul(mydatamaster.copy(), lineslength, q)
        # divtime = div(mydatamaster.copy(), lineslength, q)
        # addtime = add(mydatamaster.copy(), lineslength, q)
        # subtime = sub(mydatamaster.copy(), lineslength, q)
        
        # powtime = mypow(mydatamaster.copy(), lineslength)

        f.write('Result ' + str(i+1) + ' of ' + str(totaliteration) + '\n')
        f.write('MulTime,' + str(multime) + ',=$B$1/B' + str(3+(6*i)) + ',flop/sec,\n')
        f.write('DivTime,' + str(divtime) + ',=$B$1/B' + str(4+(6*i)) + ',flop/sec,\n')
        f.write('AddTime,' + str(addtime) + ',=$B$1/B' + str(5+(6*i)) + ',flop/sec,\n')
        f.write('SubTime,' + str(subtime) + ',=$B$1/B' + str(6+(6*i)) + ',flop/sec,\n')
        f.write('TotalTime,' + str(total_time) + ',s\n')
        # f.write('PowTime,' + str(powtime))

def mul(mydata, linecount, q):
    ret = q.get()
    start_time = t.time()
    for i in range(linecount):
        mydataline = mydata.pop()
        float(mydataline[0])*float(mydataline[1])
    total_time = t.time() - start_time;
    ret['mul'] = total_time
    q.put(ret)
    return total_time

def div(mydata, linecount, q):
    ret = q.get()
    start_time = t.time()
    for i in range(linecount):
        mydataline = mydata.pop()
        float(mydataline[0])/float(mydataline[1])
    total_time = t.time() - start_time;
    ret['div'] = total_time
    q.put(ret)
    return total_time

def add(mydata, linecount, q):
    ret = q.get()
    start_time = t.time()
    for i in range(linecount):
        mydataline = mydata.pop()
        float(mydataline[0])+float(mydataline[1])
    total_time = t.time() - start_time;
    ret['add'] = total_time
    q.put(ret)
    return total_time

def sub(mydata, linecount, q):
    ret = q.get()
    start_time = t.time()
    for i in range(linecount):
        mydataline = mydata.pop()
        float(mydataline[0])-float(mydataline[1])
    total_time = t.time() - start_time;
    ret['sub'] = total_time
    q.put(ret)
    return total_time

if __name__ == '__main__':

    main(int(sys.argv[1]))