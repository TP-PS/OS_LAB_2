import hashlib
import datetime
import multiprocessing
import itertools
import os


def f(x):
    x = ''.join(x)
    return (x, hashlib.sha256(x.encode('cp1251')).hexdigest())


def hashwriter():
    f = open('hash.txt', 'a')
    insidehashes = input()
    f.write(insidehashes + '\n')
    f.close()


def hashreader():
    try:
        f = open("hash.txt")
        hashes = f.read()
        print(hashes)
    except FileNotFoundError:
        print("Невозможно открыть файл")


def remover():
    os.remove("hash.txt")


funcmap = {1 : hashreader, 2 : hashwriter, 3 : remover}


while __name__ == '__main__':
    print("1 for file work||2 for hash decrypt||3 for stopping")
    ans1 = int(input())
    if ans1 == 1:
        print("1 for reading from files||2 for creating a file and writing hashes||3 for deleting files||4 for stopping the prog")
        ans2 = int(input())
        if ans2 == 1:
            funcmap[1]()
        elif ans2 == 2:
            funcmap[2]()
        elif ans2 == 3:
            funcmap[3]()
        elif ans2 == 4:
            break
        else:
            print("ERR")
    elif ans1 == 2:
        with open('hash.txt') as fl:
            passwords = fl.readlines()
        count_treads = int(input('Введите количество потоков:'))
        for ps in passwords:
            print(datetime.datetime.now())
            ps = ps.strip().lower()
            if len(ps) == 0:
                continue
            with multiprocessing.Pool(count_treads) as pool:
                for s, _ in filter(lambda x: x[1] == ps,
                                   pool.imap_unordered(f, itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=5),
                                                       chunksize=1000)):
                    print(s)
        print(datetime.datetime.now())
    elif ans1 == 3:
        break
    else:
        print("ERR")



