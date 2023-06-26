from .views import *
#Se inicia el carrito 
class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        
        if not cart:
            self.session["cart"]={}
            self.cart = self.session["cart"]
        else:
            self.cart = cart
        
#Agregar un producto y cantidad
    def add(self, product):
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                "product_id": product.id,
                "name": product.name,
                "quantity": 1,
                "prices": str(product.prices),
                "image": product.image.url
                
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"]+1
                    break
        self.save()
        
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True
    
#eliminar un producto o bajar cantidad 
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value["quantity"] = value["quantity"]-1
                if value["quantity"] < 1:
                    self.remove(product)
                else:
                    self.save()
                break
            else:
                print("El producto no esta en el carrito")
    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True
        
    def totalCart(request):
        total=0
        if "cart" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["quantity"])
                return {"totalCart": total }
        