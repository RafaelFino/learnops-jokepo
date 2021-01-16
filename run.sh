#!/bin/bash
source bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8081 --log-level trace