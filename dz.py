import os
from mod_convert import conveyor
import sys
sys.setrecursionlimit(10000)


def recurs(path, dpath):
    for d in range(len(path)-1):
        revercats(direct, dpath = dpath + path[d] + '\\')

def disize(cat, score = 0):
    for get in os.scandir(cat):
        if os.path.isfile(get):
            score += get.stat().st_size
        elif os.path.isdir(get):
            score += disize(get)
    return score

def revercats(direct, dpath = ""):
    path = os.path.abspath(direct).split('\\')
    for d in range(len(path)-1):
        dpath = dpath + path[d] + '\\'
        # dpath += revercats(direct, dpath = dpath + path[d] + '\\')
        if d >= path.index(direct):
                # recurs(path, dpath)
                # print(f'{path[path.index(direct)]} - дочерняя папки {path[path.index(direct)-1]}, размер папки = {disize(dpath)} байт.')
            momsi = str(disize(dpath)) + " bytes"
            conveyor("Parent directory", path[path.index(direct)-1])
            conveyor(path[path.index(direct)], momsi)
            for get in os.listdir(dpath):
                if os.path.isfile(get):
                    filesi = str(os.path.getsize(get)) + ' bytes'
                        # print(f'{get} - файл, размер = {get.stat().st_size} байт.')
                    conveyor(get, filesi)
                elif os.path.isdir(get):
                        # print(f'{get} - папка, размер = {disize(get)} байт.')
                    dicsi = str(disize(get)) + " bytes"
                    conveyor(get, dicsi)


direct = input("2. Введите название желаемой конечной директории\n: ")
revercats(direct)