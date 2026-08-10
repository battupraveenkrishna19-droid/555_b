from fastapi import FastAPI

app=FastAPI(title="praveen")

@app.get("/")
def read_root():
    return{"Hello":"World"}
@app.get("/name")
def read_name():
    return {"name" : "praveen"}

@app.get("/batch")
def batch():
    return {"batch": "555-B" }
@app.get("/gmail")
def gmail():
    return {"gmail": "battupraveenkrishna19@gmail.com" }
