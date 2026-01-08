from fastapi import FastAPI

api = FastAPI()

@api.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows

@api.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows
