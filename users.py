
from fastapi import FastAPI
from httpx import delete
from pydantic import BaseModel

app = FastAPI()

#Inicia el server con: uvicorn users:app --reload
# uvicorn= nombre del servidor users= funciona asincrona app reload para que se cargue cada vez que hagamos cambios

#Entidad User

class User(BaseModel): # Este BaseModel nos esta dando la capacidad de crear una identidad
    id: int
    name: str
    lastname: str
    email: str
    age: int

users_list = [User(id=1, name="Cristobal", lastname="Quilimaco", email="quilimacox1@gmail.com", age=29),
                User(id=2,name="Barbara", lastname="Cordova", email="brb.cordova@gmail.com", age=31),
                User(id=3,name="Justin", lastname="Lastame", email="bieber@gmail.com", age=29)]

#Obligatorio: tipar los datos para que no se puedan sobreescribir

@app.get("/usersjson")
async def users():  #Siempre que llamamos a un servidor la peticion debe ser asincrona
    return [{"name": "Cristobal", "lastname": "Quilimaco", "email": "quilimacox1@gmail.com", "age": 29},
    {"name": "Barbara", "lastname": "Cordova", "email": "brb.cordova@gmail.com", "age": 31},
    {"name": "Justin", "lastname": "Bieber", "email": "bieber@gmail.com", "age": 29}]

@app.get("/users") #Se define el path 
async def users():
    return users_list


#----PATH
@app.get("/user/{id}") #Se define path
async def user(id: int):
    return search_user(id)
    

#----QUERY
@app.get("/user/") #Se define Path
async def user(id: int):
    return search_user(id)


    ###----POST   ------ metodo para agregar un nuevo usuario
@app.post("/user/") #Defnir path 
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"Error: El usuario ingresado ya existe"}
    else:
            users_list.append(user)

#------ PUT----- Metodo para actualizar un usuario 

@app.put("/user/") #se define el path
async def user(user: User):

    found = False # Se utiliza como indicador para ver si se encontro el usuario en "users_list" y que coincida con el id que esta intentando actualizar

    for index, save__user in enumerate(users_list): #Con el bucle for se recorre todos los elementos del "user_list"  con enumerate para obtener tanto el indice como el usuario en cada iteracion
        if save__user.id == user.id:  #Despues de recorrer el arreglo se encuenta la coincidencia del id del usuario este se guarda y se procede a actualizar
            users_list[index] = user
            found = True
    
    if not found:  #Si despues de hacer el recorrido en la lista de usuarios el estado de foun sigue siendo falso retorna el siguiente mensaje:
        return {"Error: El usuaro no se puede actualizar"}
    

#-------------------DELETE-------   metodo para eliminar un usuario
@app.delete("/user/{id}")
async def delete_user(id: int): #Declarar el valor del item como int para que lo pueda buscar como numero
    found = False      #Se uriliza como indicador para saber si se encontro el item

    for index, user in enumerate(users_list): # Se recoren todos los elementos de "user_list" y con enumerate para obtener tanto el indice como el usuario en cada iteracion
        if user.id == id:  #Despues de recorrer el arreglo si se encuentra alguna coincidencia con el id del usuario se procede a hacer la eliminacion
            del users_list[index] 
            found = True

    if not found:       #Si el usuario no se encuentra se retorna el mensaje:
        return {"Error: El usuario no se encontró"}



def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error: No se ha encontrado el usuario"}