#create by SongXY
#Created on: 2016.3.7
#update: 2016.3.7
import pymongo

class infoSearch():
    
    def linkdatabase(self):
        
        client = pymongo.MongoClient("localhost",27017)
        db = client.shiyan
        collection = db.person 
        print("Please input the key of the protein,Example:cui")
        key = input()        
        for data in collection.find({"name":{'$regex':key}}):
            print(data)
        
     

           
    
 