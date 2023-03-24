import pickle
  
def storeData():
    shinobi = {
        "Gaara" : "Sand Ninja",
        "Naruto": "Leaf Ninja",
        "Jiraiya" : "Pervy Sage"
    } 
   
    with open('11B-file', 'wb') as f:
        pickle.dump(shinobi, f)
  
def loadData():
    with open('11B-file', 'rb') as f:
        shinobi = pickle.load(f)
        for k, v in shinobi.items():
            print(k, '=>', v)
  
storeData()
loadData()