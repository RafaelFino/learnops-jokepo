#!/usr/bin/python3
from fastapi import FastAPI
from datetime import datetime
from entities.game import *

app = FastAPI()
instance = Game()


@app.get("/ping")
async def pong():
    return {"pong": datetime.now().time()}

@app.get("/paper")
async def Paper():
    return instance.Execute("P")

@app.get("/rock")
async def Rock():
    return instance.Execute("R")

@app.get("/scisor")
async def Scisor():
    return instance.Execute("S")

@app.get("/stats")
async def Paper():
    return instance.Stats()


