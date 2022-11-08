import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://LisehdZarate:123@atlascluster.cui34na.mongodb.net/?retryWrites=true&w=majority",
tlsCAFile=ca)

#db = client.test
#print(db)

baseDatos = client["bd_registraduria"]
print(baseDatos.list_collection_names())