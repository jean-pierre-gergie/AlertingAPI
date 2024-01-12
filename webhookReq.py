from fastapi import FastAPI
from fastapi import  Response,Request, HTTPException
import requests


app = FastAPI()

@app.post("/")
async def read_root(request: Request):
    # try:
    #     payload = await request.json()
    #     print("Payload:", payload)
    #     alert = payload['alerts'][0]
    #     values = alert.get('values', {})
    #     value_a = values.get('A', None)
    #     value_b = values.get('B', None)
    #     value_c = values.get('C', None)
    #     print(value_a)
    #     if value_c ==1:
    #         stt="Firing"
    #     else:
    #         stt= "Normal"
    #     message = f" High RAM Utilization {value_a}; AlERT STATUS: {stt}."




    #     return {"message": "Request processed successfully"}
    # except Exception as e:
    #     # raise HTTPException(status_code=500, detail=str(e))
    #     pass

    url = "https://waba.360dialog.io/v1/messages/"

    payload = '''
       {
        "to": "96171882544",
        "type": "template",
        "template": {
        "namespace": "241bdffc_373b_44ec_861e_03a8c5749b3b",
            "language": {
                "policy": "deterministic",
                "code": "AR"
            },
            "name": "seamless_thanks"  

        }
    }
    '''

    headers = {
        'D360-Api-Key': "EFhJ97DqrPXG9B9HD1pygw2dAK",
        'Content-Type': "application/json",
    }

    response = requests.post(url, data=payload, headers=headers)
    print(response.status_code)





    return {"message": 'OK'}

