import pickle
  
def storeData():
    RockLee = {'Name' : 'Rock Lee', 'Affiliation' : 'Konohagakure ', 'age' : 28, 'jutsu' : 'Eight Gates'}
    Gaara = {'Name' : 'Gaara of The Sand', 'Affiliation' : 'Sunagakure', 'age' : 18, 'jutsu' : 'Sand Coffin'}


    shinobis = {'RockLee': RockLee, 'Gaara': Gaara}
    with open('11B-file', 'ab') as f:
        pickle.dump(shinobis, f)
  
def loadData():
    with open('11B-file', 'rb') as f:
        shinobis = pickle.load(f)
        for k, v in shinobis.items():
            print(k, '=>', v)
  

storeData()
loadData()