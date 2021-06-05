# 
# Exemplo de acesso a uma base de dados SQLite
#

import pymongo import MongoClient

def manipulaDadosMongoDB():
    cliente = pymongo.MongoClient("mongodb://localhost:27017")
    db = cliente.conheca_python

    for i in range(1, 10):
        objDic = {'código' :i}
        db.conheca_python.insert_one(objDic)

    db.conheca_mongodb.update_one({'código' :2}, {"$set" : {'atributoNovo' : 789}}) 
    db.conheca_mongodb.delete_one({'código' : 1})
    
    resultadoConsulta = db.conheca_mongodb.find({})
    for doc in resultadoConsulta:
        print (doc)

manipulaDadosMongoDB()
 