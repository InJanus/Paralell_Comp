import tqdm as tq
import time as t
import sys


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
    f.write('Total Number of Lines,' + str(lineslength) + '\n')
    for i in tq.tqdm(range(totaliteration), desc="Running Benchmarks…", ascii=False, ncols=100):

        multime = mul(mydatamaster.copy(), lineslength)
        divtime = div(mydatamaster.copy(), lineslength)
        addtime = add(mydatamaster.copy(), lineslength)
        subtime = sub(mydatamaster.copy(), lineslength)
        
        # powtime = mypow(mydatamaster.copy(), lineslength)

        f.write('Result ' + str(i+1) + ' of ' + str(totaliteration) + '\n')
        f.write('MulTime,' + str(multime) + ',=$B$1/B' + str(3+(6*i)) + ',flop/sec,\n')
        f.write('DivTime,' + str(divtime) + ',=$B$1/B' + str(4+(6*i)) + ',flop/sec,\n')
        f.write('AddTime,' + str(addtime) + ',=$B$1/B' + str(5+(6*i)) + ',flop/sec,\n')
        f.write('SubTime,' + str(subtime) + ',=$B$1/B' + str(6+(6*i)) + ',flop/sec,\n\n')

        # f.write('PowTime,' + str(powtime))

def mul(mydata, linecount):
    start_time = t.time()
    for i in range(linecount):
        mydataline = mydata.pop()
        float(mydataline[0])*float(mydataline[1])
    total_time = t.time() - start_time;
    return total_time

def div(mydata, linecount):
    start_time = t.time()
    for i in range(linecount):
        mydataline = mydata.pop()
        float(mydataline[0])/float(mydataline[1])
    total_time = t.time() - start_time;
    return total_time

def add(mydata, linecount):
    start_time = t.time()
    for i in range(linecount):
        mydataline = mydata.pop()
        float(mydataline[0])+float(mydataline[1])
    total_time = t.time() - start_time;
    return total_time

def sub(mydata, linecount):
    start_time = t.time()
    for i in range(linecount):
        mydataline = mydata.pop()
        float(mydataline[0])-float(mydataline[1])
    total_time = t.time() - start_time;
    return total_time

def mypow(mydata, linecount):
    start_time = t.time()
    for i in range(linecount):
        mydataline = mydata.pop()
        pow(float(mydataline[0]),float(mydataline[1]))
    total_time = t.time() - start_time;
    return total_time

if __name__ == '__main__':
    main(int(sys.argv[1]))