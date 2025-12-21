from shopping.cart import orderCart
try:
    product_name = str(input("Enter the Product name: "))
    categroy     = str(input("Enter the Product category: "))
    if product_name.isdigit():
        raise ValueError("Product Name must be string")
    if categroy.isdigit():
        raise ValueError("Categroy must be a string")
    price        = float(input("Enter the price: "))
    qty          = int(input("Enter the Qty: "))
    
except ValueError as e:
    print(f"Your input error {e}")
else:
    product = {
        "product_name" :product_name,
        "categroy" : categroy,
        "price" : price,
        "qty" : qty
    }
    print(orderCart.add_cart(product))
finally:
   print("Your product process successfully") 