from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print(0.2568 + 4.5689)
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('brian',))
    p.start()
    p.join()