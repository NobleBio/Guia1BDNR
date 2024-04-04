from pymongo import MongoClient

# Connection Details
DATABASE_NAME = 'DataBase'
COLLECTION_NAME = 'Collection'
MONGO_URI = 'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.2'

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]


def create_document():
    name = input("Ingrese el nombre del restaurante: ")
    building = input("Ingrese el número de edificio: ")
    street = input("Ingrese el nombre de la calle: ")
    zipcode = input("Ingrese el código postal: ")
    borough = input("Ingrese el distrito: ")
    cuisine = input("Ingrese el tipo de cocina: ")
    
    coord_lon = float(input("Ingrese la longitud de coordenada: "))
    coord_lat = float(input("Ingrese la latitud de coordenada: "))
    coordinates = [coord_lon, coord_lat]
    
    grade = input("Ingrese el grado (e.g., A, B, C): ")
    score = int(input("Ingrese la nota: "))


    new_document = {
        "name": name,
        "address": {
            "building": building,
            "street": street,
            "zipcode": zipcode,
            "coord": coordinates,
        },
        "borough": borough,
        "cuisine": cuisine,
        "grades": [
            {"grade": grade, "score": score}
        ],
    }
    collection.insert_one(new_document)
    print("¡Documento creado!")

def read_documents():
    documents = collection.find()
    for doc in documents:
        print(doc)


def update_document():
    filter_field = input("Ingrese el campo para buscar (ej., name): ")
    filter_value = input(f"Ingrese el valor de {filter_field}: ")

    update_field = input("Ingrese el campo a actualizar (ej., name):")
    new_value = input(f"Ingrese el nuevo valor para {update_field}: ")

    result = collection.update_one({filter_field: filter_value}, {"$set": {update_field: new_value}})
    if result.modified_count:
        print("Documento actualizado")
    else:
        print("Documento no encontrado")


def delete_document():
    restaurant_id = input("Ingrese el ID del restaurante: ")
    result = collection.delete_one({"restaurant_id": restaurant_id})
    if result.deleted_count:
        print("¡Documento eliminado!")
    else:
        print("Documento no encontrado.")

#  Menu
while True:
    print("\nElija una operación")
    print("1. Crear")
    print("2. Leer Todos los Documentos")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Salir")

    choice = input("Ingrese su eleccion : ")

    if choice == '1':
        create_document()
    elif choice == '2':
        read_documents()
    elif choice == '3':
        update_document()
    elif choice == '4':
        delete_document()
    elif choice == '5':
        break
    else:
        print("Opcion invalida. Por favor, intente de nuevo.")

# Close MongoDB connection
client.close()
