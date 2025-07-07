from fastapi import FastAPI
import random as rd

app = FastAPI()

list = ['Jurassic Park', 'Roli szar filmje', 'Jupi és Eddie Murphy', 'hihetetlen, hogy még nem írtam rá', 'Dáviddal tali']


@app.get("/idea")
def get_random_idea():
	x = rd.choice(list)
	return {"idea": x}