from fastapi import FastAPI
from fastapi import  Response,Request, HTTPException










app = FastAPI()

@app.post("/")
async def read_root(request: Request):
    try:
        payload = await request.json()
        print("Payload:", payload)
        alert = payload['alerts'][0]
        values = alert.get('values', {})
        value_a = values.get('A', None)
        value_b = values.get('B', None)
        value_c = values.get('C', None)
        print(value_a)
        if value_c ==1:
            stt="Firing"
        else:
            stt= "Normal"
        message = f" High RAM Utilization {value_a}; AlERT STATUS: {stt}."




        return {"message": "Request processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": 'OK'}

if __name__ == "__main__":
    import uvicorn


    uvicorn.run(app, host="0.0.0.0", port=9001)