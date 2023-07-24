import os
import sys
sys.setrecursionlimit(10000)


def recurs(path, dpath):
    for d in range(len(path)-1):
        revercats(direct, dpath = dpath + path[d] + '\\')

def disize(cat, total = 0):
    for get in os.scandir(cat):
        if os.path.isfile(get):
            total += os.path.getsize(get)
        elif os.path.isdir(get):
            total += disize(get)
    return total

def revercats(direct, dpath = ""):
    path = os.path.abspath(direct).split('\\')
    for d in range(len(path)-1):
        dpath = dpath + path[d] + '\\'
        if d >= path.index(direct):
            # recurs(path, dpath)
            # print('\n', os.listdir(dpath))
            print(f'{path[path.index(direct)]} - дочерняя папки {path[path.index(direct)-1]}, размер {disize(dpath)}')
            for get in os.scandir(dpath):
                if os.path.isfile(get):
                    print(f'{get} - файл')
                elif os.path.isdir(get):
                    print(f'{get} - папка')

direct = input("2. Введите название желаемой конечной директории\n: ")
revercats(direct)   