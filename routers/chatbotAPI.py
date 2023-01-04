from fastapi import APIRouter,Request,HTTPException,Response,Depends
import requests
from func.func import kiemtratuoi,nhapgioitinh,nhaptuoi,welcome,loaido,reset,chonmua,chondip,chonbenh,chondakichung,chonphongcach,nhaplai,chonvai,nhapcannang,nhapchieucao,tinhsize
from func.func import chontoneda,final
import models
from database import get_db
from sqlalchemy.orm import Session


PAGE_ACCESS_TOKEN = "EAAJ82f1tJw8BAOSjNClnG0RkjjSldlVcKzI37qk1ohBpo1B8Vm3lZAWB5hdUP7iEyZCUZBZC7QUrzyHI2u5X6bjrZBSkk6hrKFnNnkAwtqILoZA2OsQmbZBZA4DRSJpbWWHNmGWpdfgP84q4NSEWCziAosKP0hgNnhYQNuvZCwYtn2VArEDmPztMx"
VERIFY_TOKEN = "ngothenghia"
API = "https://graph.facebook.com/v13.0/me/messages?access_token="+ PAGE_ACCESS_TOKEN

router = APIRouter(tags=['ChatBotAPI'])

# @router.get("/")
# def getHomePage():
#     return "Ngô Thế Nghĩa" 

@router.get("/")
def fbverify(request: Request):
    mode = request.query_params.get("hub.mode");
    token = request.query_params.get("hub.verify_token");
    challenge = request.query_params.get("hub.challenge");
    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN :
            print("WEBHOOK_VERIFIED")
            return Response(content=challenge,status_code=200)
        else:
            raise HTTPException(status_code=403,detail= "Verification token missmatch")
    return "Ngô Thế Nghĩa"


@router.post("/")
async def postWebhook(request: Request, db : Session =Depends(get_db)):
    data = await request.json()
    print(data)
    try:
        # Read messages from facebook messanger.
        message = data['entry'][0]['messaging'][0]['message']
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']
        try : 
            user = db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id).first()
        except : 
            print("0")
        welcome(sender_id=sender_id,message=message,db=db)
        nhapgioitinh(sender_id=sender_id,message=message,db=db)
        if user.loaituvan != None and user.gioitinh == None and user.chieucao == None and user.cannang==None :
            nhaptuoi(sender_id=sender_id,message=message,db=db)
        elif user.gioitinh != None and user.age_type == None:
            kiemtratuoi(sender_id=sender_id,message=message,db=db)
        elif user.age_type != None and user.loaido == None:
            loaido(sender_id=sender_id,message=message,db=db)
        elif user.loaido != None and user.mua == None:
            chonmua(sender_id=sender_id,message=message,db=db)
        elif user.mua != None and user.dip == None:
            chondip(sender_id=sender_id,message=message,db=db)
        elif user.dip != None and user.end != 1 and user.gioitinh == "Nữ" and user.phongcach == None and user.da == None :
            chonphongcach(sender_id=sender_id,message=message,db=db)
        elif user.dip != None and user.end != 1 and user.da == None and user.phongcach == None and ( user.age_type == "Thiếu Nhi"  or  user.age_type == "Cao Tuổi") :
            chondakichung(sender_id=sender_id,message=message,db=db)
            chonbenh(sender_id=sender_id,message=message,db=db)
        elif user.loaituvan != None and user.gioitinh != None and user.loaido != None and user.mua != None and user.dip != None and user.loaivai == None:
            chonvai(sender_id=sender_id,message=message,db=db)
        elif user.loaituvan != None and user.gioitinh != None and user.loaido != None and user.mua != None and user.dip != None and user.loaivai != None and user.chieucao == None:
            nhapchieucao(sender_id=sender_id,message=message,db=db)
        elif user.loaituvan != None and user.gioitinh != None and user.loaido != None and user.mua != None and user.dip != None and user.loaivai != None and user.chieucao != None and user.cannang == None:
            nhapcannang(sender_id=sender_id,message=message,db=db)
            tinhsize(sender_id=sender_id,db=db)
        elif user.loaituvan != None and user.gioitinh != None and user.loaido != None and user.mua != None and user.dip != None and user.loaivai != None and user.chieucao != None and user.cannang != None and user.mauda == None:
            chontoneda(sender_id=sender_id,message=message,db=db)
        else:
            nhaplai(sender_id=sender_id,message=message)
            

        reset(sender_id=sender_id,message=message,db=db)
        
    except:
        print("Main")

