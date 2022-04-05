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


def textbroot():
    with open('hash.txt') as fhash:
        passwords = fhash.readlines()
    count_treads = int(input('Введите количество потоков:'))
    print(datetime.datetime.now())
    for ps in passwords:
        ps = ps.strip().lower()
        if len(ps) == 0:
            continue
        with multiprocessing.Pool(count_treads) as pool:
            for s, _ in filter(lambda x: x[1] == ps, pool.imap_unordered(f, itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=5), chunksize=1000)):
                print(s)
                print(datetime.datetime.now())


funcmap = {1 : hashreader, 2 : hashwriter, 3 : remover, 4 : textbroot}


if __name__ == '__main__':
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
            elif ans2 == 5:
                break
            else:
                print("ERR")
        elif ans1 == 2:
                print("1 for brooting from file||2 for brooting from console||3 for stopping the prog ")
                ans3 = int(input())
                if ans3 == 1:
                     funcmap[4]()
                elif ans3 == 2:
                        file = open('onlinehash.txt', 'a')
                        insidehashes = str(input())
                        file.write(insidehashes + '\n')
                        file.close()
                        with open('onlinehash.txt') as fhash:
                            passwords = fhash.readlines()
                        count_treads = int(input('Введите количество потоков:'))
                        print(datetime.datetime.now())
                        for ps in passwords:
                            ps = ps.strip().lower()
                            if len(ps) == 0:
                                continue
                            with multiprocessing.Pool(count_treads) as pool:
                                for s, _ in filter(lambda x: x[1] == ps, pool.imap_unordered(f, itertools.product(
                                        'abcdefghijklmnopqrstuvwxyz', repeat=5), chunksize=1000)):
                                    print(s)
                                    print(datetime.datetime.now())
                        os.remove("onlinehash.txt")
                elif ans2 == 3:
                    break
                else:
                    print("ERR")
        else:
            print("ERR")



