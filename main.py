from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():  #Siempre que llamamos a un servidor la peticion debe ser asincrona
    return "Hola mundo prueba"

@app.get("/url")
async def url():  
    return { "url":"https://.teguilog.com" }
