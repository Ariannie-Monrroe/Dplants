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
        if str(product.slug) not in self.cart.keys():
            self.cart[product.id] = {
                "product_id": product.slug,
                "name": product.name,
                "stock": product.stock,
                "prices": str(product.prices),
                "image": product.image.url,
                "quantity": 1,
            }
        else:
            # self.cart[product.slug]["quantity"] +=1
            # self.cart[product.slug]['prices'] +=product.prices
            for key, value in self.cart.items():
                if key == str(product.slug):
                    value["quantity"]+=1
                    
                    
                
        self.save()
        
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True
    
#eliminar un producto o bajar cantidad 
    def remove(self, product):
        product_id = str(product.slug)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.slug):
                value["quantity"] -=1
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
        
    
        