#!/usr/bin/python3
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
from entities.game import *

app = FastAPI()
instance = Game()

@app.get("/ping")
async def pong():
    return {"pong": datetime.now().time()}

@app.post("/paper")
async def Paper():
    return instance.Execute("P")

@app.post("/rock")
async def Rock():
    return instance.Execute("R")

@app.post("/scisor")
async def Scisor():
    return instance.Execute("S")

@app.get("/stats")
async def Paper():
    return instance.Stats()

@app.get("/", response_class=HTMLResponse)
async def Home():
	f = open("web/index.html", "r")
	home = f.read()
	f.close()
	return home

