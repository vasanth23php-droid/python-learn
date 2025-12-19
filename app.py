from flask import Flask,request,json

app = Flask(__name__)

store = [
    {
        "store_name" : "ASV Store",
        "Items" : [
            {
            "product" : "Table",
            "price" : 66.96 
            }
        ]
    }
]
@app.get("/store")
def get_store():
    return store,201
@app.post("/store")
def add_store():
    request_data = request.get_json()
    new_store = { "store_name": request_data["store_name"], "Items": [] }
    store.append(new_store)
    return "Successfully Added", 201
@app.post("/store/<string:name>/additem")
def add_item_store(name):
    request_data = request.get_json()
    for storeitems in store:
        if storeitems['store_name'] == name:
            new_item = {"product": request_data['product'], "price": request_data['price']}
            storeitems['Items'].append(new_item)
            return f"Successfully Added Item {name}",201
    return "Store Not Found",201
@app.get("/store/<string:name>/getitem")
def fetch_item(name):
    for storeitems in store:
        if storeitems['store_name'] == name:
            return {"Items" : storeitems['Items']},201
    return "store not found",201


