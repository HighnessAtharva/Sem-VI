import pickle
  
def storeData():
    Shinobi1 = {'Name' : 'Rock Lee', 'Affiliation' : 'Konohagakure ', 'age' : 28, 'jutsu' : 'Eight Gates'}
    Shinobi2 = {'Name' : 'Gaara of The Sand', 'Affiliation' : 'Sunagakure', 'age' : 18, 'jutsu' : 'Sand Coffin'}


    shinobis = {'NinjaData#1': Shinobi1, 'NinjaData#2': Shinobi2}
    with open('11B-file', 'ab') as f:
        pickle.dump(shinobis, f)
  
def loadData():
    with open('11B-file', 'rb') as f:
        shinobis = pickle.load(f)
        for keys in shinobis:
            print(keys, '=>', shinobis[keys])
  

storeData()
loadData()