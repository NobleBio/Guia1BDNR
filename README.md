# Guia 1 Base de Datos No Relacionales

## README

**Introducción**

Este README describe cómo configurar y ejecutar un CRUD (Crear, Leer, Actualizar, Eliminar) con MongoDB y Python en Ubuntu.

**Requisitos:**

* Ubuntu
* Python 3
* MongoDB
* Entorno virtual Python (venv)

**Instalación:**

**1. Instalar el módulo venv:**

```
sudo apt install python3-venv
```

**2. Crear el entorno virtual:**

```
python3 -m venv venv-python3
```

**3. Activar el entorno virtual:**

```
source venv-python3/bin/activate
```

**4. Instalar las dependencias:**

```
pip install pymongo
```

**5. Importar la colección JSON a MongoDB:**

```
mongoimport --db test --collection restaurants --drop --file dataset.json
```

**6. Iniciar MongoDB:**

```
sudo service mongod start
```

**7. Verificar el estado de MongoDB:**

```
sudo service mongod status
```

**8. Iniciar el servicio mongosh:**

```
mongosh
```

**9. Verificar las colecciones:**

```
show collections
```

**10. Ejecutar el script CRUD:**

```
Guia1.py
```

**Conexión a la BD:**

El programa utiliza la biblioteca pymongo para conectarse a la base de datos MongoDB. La configuración de la conexión se realiza en el script Guia1BDNR.py.

**Esquema de la BD:**

La base de datos utilizada en este programa tiene una sola colección llamada "Collection". La colección "Collection" tiene los siguientes campos:

* _id: Identificador único del documento (generado automáticamente por MongoDB)
* Nombre: Nombre del elemento
* Apellido: Apellido del elemento
* Edad: Edad del elemento
* Telefono: Telefono del elemento
* Correo: Correo del elemento

**Descripción del script CRUD:**

* `create_document()`: Crea un nuevo documento en la colección.
* `read_documents()`: Lee y muestra todos los documentos de la colección.
* `update_document()`: Actualiza un documento en la colección.
* `delete_document()`: Elimina un documento de la colección.

**Menú:**

El script presenta un menú interactivo que permite al usuario realizar las siguientes operaciones:

* 1. Crear
* 2. Leer
* 3. Actualizar
* 4. Eliminar
* 5. Salir

**Nota:**

* El script está configurado para usar la base de datos "DataBase" y la colección "Collection".
* Asegúrese de reemplazar los nombres de la base de datos y la colección si es necesario.

