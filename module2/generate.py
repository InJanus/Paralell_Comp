import random as r
import time
import tqdm as tq
import sys

def main(datapoints):
    # generate numbers for benchmarking
    f = open('data/data.csv', 'w')
    r.seed(time.time())
    for i in tq.tqdm(range(datapoints), desc="Loading…", ascii=False, ncols=100):
        randomfloat1 = ((r.random()*1000000)+1)
        randomfloat2 = ((r.random()*1000000)+1)
        outputline = str(randomfloat1) + ',' + str(randomfloat2) + '\n';
        f.write(outputline)
    print("Complete.")

if __name__=='__main__':
    main(int(sys.argv[1]))