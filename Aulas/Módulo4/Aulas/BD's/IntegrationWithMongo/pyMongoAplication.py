import pymongo as pym
import datetime

cliente = pym.MongoClient("mongodb+srv://brnomort1:brnomort1@cluster0.yiejpab.mongodb.net/?retryWrites=true&w=majority")
db = cliente.test
collection = db.test_collection

print(db.test_collection)

post = { # definição de doc(file)
    "autor" : "Mike",
    "text" : "My first mongodb application base with python3",
    "tag_id" : ["mongodb","python3","pymongo"],
    "date" : datetime.date.today(),
}

# Preparando para submeter as informações
posts = db.post
post_id = posts.insert_one(post).inserted_id
print(post_id)