from fastapi import FastAPI
app = FastAPI(title="Edvora _ The New Dawn of Education in Africa")
@app.get("/")
async def read_root():
    return {"message": "Hello — FastAPI is running (Edvora _ The New Dawn of Education in Africa)!"}
@app.get("/health")
async def health_check():
    return {"status": "ok"}
