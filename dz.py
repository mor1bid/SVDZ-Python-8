import os
# import json
# import csv
from mod_csvconvert import csv_process
from mod_jsonconvert import json_process
import pickle
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
        with open ("datarecord.json", "w+", encoding= 'utf-8') as json_rec:
            if d >= path.index(direct):
                # recurs(path, dpath)
                # print(f'{path[path.index(direct)]} - дочерняя папки {path[path.index(direct)-1]}, размер папки = {disize(dpath)} байт.')
                momsi = str(disize(dpath)) + " bytes"
                json_process("Parent directory", path[path.index(direct)-1])
                json_process(path[path.index(direct)], momsi)
                csv_process("Parent directory", path[path.index(direct)-1])
                csv_process(path[path.index(direct)], momsi)
                # json.dump([{"Parent directory": path[path.index(direct)-1], path[path.index(direct)]: momsi}], json_rec, indent= 2)
                for get in os.listdir(dpath):
                    if os.path.isfile(get):
                        filesi = str(os.path.getsize(get)) + ' bytes'
                        # print(f'{get} - файл, размер = {get.stat().st_size} байт.')
                        # json.dump([{get: filesi}], json_rec, indent= 2)
                        json_process(get, filesi)
                        csv_process(get, filesi)
                    elif os.path.isdir(get):
                        # print(f'{get} - папка, размер = {disize(get)} байт.')
                        dicsi = str(disize(get)) + " bytes"
                        # json.dump([{get: dicsi}], json_rec, indent= 2)
                        json_process(get, dicsi)
                        csv_process(get, dicsi)
        json_rec.close()


direct = input("2. Введите название желаемой конечной директории\n: ")
revercats(direct)