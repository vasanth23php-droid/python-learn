def add_cart(cart):
    cartDictionary = {}
    for key, value in cart.items():
        cartDictionary.update({key:value})
    cartDictionary['amount'] = cartDictionary['price'] * cartDictionary['qty']
    return cartDictionary