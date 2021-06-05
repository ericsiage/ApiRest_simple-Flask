from flask import Flask, jsonify, request
#jsonify nos permite convertir objetos en objetos json.
#render_template renderiza los templates, los carga
#request recibe los datos del metodo post.

from products import products

#create flask instance.
app = Flask(__name__) #encuentra los directorios




#Creacion de rutas.
@app.route('/test')
def test():
    return jsonify({"message": "pong"})

#Todos los productos
@app.route('/products')
def getProducts():
    return jsonify(products)

#productos por nombre.
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name']==product_name]
    if (len(productsFound) > 0):
        return jsonify({"product":productsFound[0]})
    else:
        return jsonify({"message": "product not found"})

#Agregar productos
@app.route('/Products', methods=['GET', 'POST'])
def addProducts():
    new_product= {
        "id": request.json['id'],
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity'],
    }
    products.append(new_product) #agregamos new_product a products.
    return jsonify({"message": "product added succesfully", "products": products})


#Actualizar productos 
@app.route('/products/<string:product_name>', methods=['GET', 'PUT'])
def updateProduct(product_name):
    productsFound = [product for product in products if product['name']==product_name] #bucle producto por producto en la lista products si name es igual a product_name.
    if (len(productsFound) > 0):
        productsFound[0]['id'] = request.json['id'],
        productsFound[0]['name'] = request.json['name'],
        productsFound[0]['price'] = request.json['price'],
        productsFound[0]['quantity'] = request.json['quantity'],
        return jsonify({
            "message": "Product Updated",
            "product":productsFound[0] 
            })#devolvemos un mensaje con el producto actualizado..
    else:
        return jsonify({"message": "product not found"})

#Borrar productos.
@app.route('/products/<string:product_name>', methods=['GET', 'DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name']==product_name]
    if (len(productsFound) > 0):
        products.remove(productsFound[0])
        return jsonify({"message": "Product deleted",
                        "products": products
                        })
    else:
        return jsonify({"message": "product not found"})




#run with debug
if __name__== '__main__':
    app.run(debug=True, port=4000)