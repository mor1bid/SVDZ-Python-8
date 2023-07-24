import csv
import json
import pickle

def pickle_process(key, value):
    with open ("datarecord.pickle", "ab+") as pickle_rec:
        pickle.dump([{key: value}], pickle_rec, protocol=pickle.HIGHEST_PROTOCOL)
    pickle_rec.close()

def json_process(key, value):
    with open ("datarecord.json", "a+", encoding= 'utf-8') as json_rec:
        json.dump([{key: value}], json_rec, indent= 2)
    json_rec.close()

def csv_process(key, value):
    with open ("datarecord.csv", 'a+', newline='', encoding= 'utf-8') as csv_rec:
        rec = csv.writer(csv_rec, delimiter=' ')
        rec.writerow([key] + [value])
    csv_rec.close()

def conveyor(key, value):
    csv_process(key, value)
    json_process(key, value)
    pickle_process(key, value)