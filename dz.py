import os
import sys
sys.setrecursionlimit(10000)

def revercats(direct, dpath = ""):
    path = os.path.abspath(direct).split('\\')
    for d in range(len(path)-1):
        #dpath = dpath + path[d] + '\\'
        if d >= path.index(direct):
            revercats(direct, dpath = dpath + path[d] + '\\')
            # print('\n', os.listdir(dpath))
            for get in os.listdir(d):
                if os.path.isfile(get):
                    print(f'{get} - файл')
                elif os.path.isdir(get):
                    print(f'{get} - папка')

direct = input("2. Введите название желаемой конечной директории\n: ")
revercats(direct)   