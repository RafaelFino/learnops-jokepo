#!/usr/bin/python3
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
from service.game import *

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

@app.post("/scissor")
async def Scissor():
    return instance.Execute("S")

@app.get("/stats")
async def Stats():
    return instance.Stats()

@app.get("/", response_class=HTMLResponse)
async def Home():
	f = open("web/index.html", "r")
	home = f.read()
	f.close()
	return home

@app.get("/test")
async def Test():
	instance.Test(10000)
	return instance.Stats()
		