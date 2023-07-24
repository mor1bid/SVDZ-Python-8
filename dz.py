import os
from mod_convert import conveyor
import sys
sys.setrecursionlimit(10000)

def recycle(direct, dpath = ""):
    path = os.path.abspath(direct).split('\\')
    for d in range(len(path)-1):
        dpath = dpath + path[d] + '\\'
        for re in os.listdir(dpath):
            if 'datarecord' in re and d >= path.index(direct):
                os.remove(re)

def disize(cat, score = 0):
    for get in os.scandir(cat):
        if os.path.isfile(get):
            score += get.stat().st_size
        elif os.path.isdir(get):
            score += disize(get)
    return score

def revercats(direct, dpath = "", d = 0):
    path = os.path.abspath(direct).split('\\')
    path.pop(-1)
    if d >= path.index(direct):
        momsi = str(disize(dpath)) + " bytes"
        conveyor("Parent directory", path[path.index(direct)-1])
        conveyor(path[path.index(direct)], momsi)
        for get in os.listdir(dpath):
            if os.path.isfile(get):
                filesi = 'file ' + str(os.path.getsize(get)) + ' bytes'
                conveyor(get, filesi)
            elif os.path.isdir(get):
                dicsi = 'directory ' + str(disize(get)) + " bytes"
                conveyor(get, dicsi)
    if d != len(path):
        return revercats(direct, dpath + path[d] + '\\', d + 1)

direct = input("2. Введите название желаемой конечной директории\n: ")
recycle(direct)
revercats(direct)
print("Выполнено!")