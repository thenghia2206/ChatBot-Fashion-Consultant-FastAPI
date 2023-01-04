# from fastapi import Depends
import requests
import models
import math
from predict import predict
from CBR.CBR import CBR
# from database import get_db
# from sqlalchemy.orm import  Session
# db: Session = Depends(get_db)

PAGE_ACCESS_TOKEN = "EAAJ82f1tJw8BAOSjNClnG0RkjjSldlVcKzI37qk1ohBpo1B8Vm3lZAWB5hdUP7iEyZCUZBZC7QUrzyHI2u5X6bjrZBSkk6hrKFnNnkAwtqILoZA2OsQmbZBZA4DRSJpbWWHNmGWpdfgP84q4NSEWCziAosKP0hgNnhYQNuvZCwYtn2VArEDmPztMx"
VERIFY_TOKEN = "ngothenghia"
API = "https://graph.facebook.com/v13.0/me/messages?access_token=" + PAGE_ACCESS_TOKEN


def welcome(sender_id, message, db):
    if str(message['text']).lower().strip() == "hello":
        request_body = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "Chào Mừng Bạn Đến Với Chat Bot Tư Vấn Làm Đẹp !"
            }
        }
        request_body1 = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "Bạn muốn tư vấn về quần áo hay mỹ phẩm !"
            }
        }
        request_body2 = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "(Bạn vui lòng nhập: Quần Áo hoặc Mỹ Phẩm)"
            }
        }
        user = db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id)
        user_delete = user.first()
        if user_delete:
            user.delete(synchronize_session=False)
            db.commit()
        response = requests.post(API, json=request_body).json()
        requests.post(API, json=request_body1).json()
        requests.post(API, json=request_body2).json()
        return response


def nhapgioitinh(sender_id, message, db):
    if str(message['text']).lower().strip() == "quần áo":
        request_body_1 = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "Bạn Vui Lòng Nhập giới tính :"
            }
        }
        request_body_2 = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "(Bạn vui lòng nhập : Nam hoặc Nữ )"
            }
        }
        user = models.CaseIn(id_fb=sender_id, loaituvan = "Quần Áo")
        db.add(user)
        db.commit()
        db.refresh(user)
        response = requests.post(API, json=request_body_1).json()
        requests.post(API, json=request_body_2).json()
        return response


def nhaptuoi(sender_id, message, db):
    if str(message['text']).lower().strip() == "nam":
        request_body_1 = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "Giới tính của bạn là Nam. Bạn vui lòng nhập tuổi :"
            }
        }
        user_old = db.query(models.CaseIn).filter(
            models.CaseIn.id_fb == sender_id)
        user_old.update({"gioitinh": "Nam"}, synchronize_session=False)
        db.commit()
        response = requests.post(API, json=request_body_1).json()
        return response
    elif str(message['text']).lower().strip() == "nữ":
        request_body_1 = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "Giới tính của bạn là Nữ. Bạn vui lòng nhập tuổi :"
            }
        }
        user_old = db.query(models.CaseIn).filter(
            models.CaseIn.id_fb == sender_id)
        user_old.update({"gioitinh": "Nữ"}, synchronize_session=False)
        db.commit()
        response = requests.post(API, json=request_body_1).json()
        return response
    else :
        nhaplai(sender_id=sender_id,message=message)


def kiemtratuoi(sender_id, message, db):
    try:
        if str(message['text']).isdigit():
            if int(str(message['text']).lower().strip()) >= 6 and int(str(message['text']).lower().strip()) <= 11:
                request_body_1 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Độ tuôi bạn vừa nhập là " + str(message['text']).lower().strip() + " thuộc tuổi Thiếu Nhi"
                    }
                }
                nam = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Bạn muốn tư vấn loại đồ gì vậy. Quần hay Áo"
                    }
                }
                nu = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text":  "Bạn muốn tư vấn loại đồ gì vậy. Quần, Áo hay Váy"
                    }
                }
                user_old = db.query(models.CaseIn).filter(
                    models.CaseIn.id_fb == sender_id)
                user_old.update({"tuoi": str(message['text']).lower().strip(
                ), "age_type": "Thiếu Nhi"}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_1).json()
                if db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nam").first():
                    requests.post(API, json=nam).json()
                elif db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nữ").first():
                    requests.post(API, json=nu).json()
                return response
            elif int(str(message['text']).lower().strip()) >= 12 and int(str(message['text']).lower().strip()) <= 35:
                request_body_1 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Độ tuôi bạn vừa nhập là " + str(message['text']).lower().strip() + " thuộc tuổi Thanh-Thiếu Niên"
                    }
                }
                nam = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Bạn muốn tư vấn loại đồ gì vậy. Quần hay Áo"
                    }
                }
                nu = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text":  "Bạn muốn tư vấn loại đồ gì vậy. Quần, Áo hay Váy"
                    }
                }
                # ("Thanh-Thiếu Niên")
                user_old = db.query(models.CaseIn).filter(
                    models.CaseIn.id_fb == sender_id)
                user_old.update({"tuoi": str(message['text']).lower().strip(
                ), "age_type": "Thanh-Thiếu Niên"}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_1).json()
                if db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nam").first():
                    requests.post(API, json=nam).json()
                elif db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nữ").first():
                    requests.post(API, json=nu).json()
                return response
            elif int(str(message['text']).lower().strip()) >= 36 and int(str(message['text']).lower().strip()) <= 60:
                request_body_1 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Độ tuôi bạn vừa nhập là " + str(message['text']).lower().strip() + " thuộc tuổi Trung Niên"
                    }
                }
                nam = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Bạn muốn mua loại đồ gì vậy. Quần hay Áo"
                    }
                }
                nu = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text":  "Bạn muốn mua loại đồ gì vậy. Quần, Áo hay Váy"
                    }
                }
                # ("Trung Niên")
                user_old = db.query(models.CaseIn).filter(
                    models.CaseIn.id_fb == sender_id)
                user_old.update({"tuoi": str(message['text']).lower().strip(
                ), "age_type": "Trung Niên"}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_1).json()
                if db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nam").first():
                    requests.post(API, json=nam).json()
                elif db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nữ").first():
                    requests.post(API, json=nu).json()
                return response
            elif int(str(message['text']).lower().strip()) >= 61 and int(str(message['text']).lower().strip()) <= math.inf:
                request_body_1 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Độ tuôi bạn vừa nhập là " + str(message['text']).lower().strip() + " thuộc Cao Tuổi"
                    }
                }
                nam = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Bạn muốn mua loại đồ gì vậy. Quần hay Áo"
                    }
                }
                nu = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text":  "Bạn muốn mua loại đồ gì vậy. Quần, Áo hay Váy"
                    }
                }
                # ("Cao Tuổi")
                user_old = db.query(models.CaseIn).filter(
                    models.CaseIn.id_fb == sender_id)
                user_old.update({"tuoi": str(message['text']).lower().strip(
                ), "age_type": "Cao Tuổi"}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_1).json()
                if db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nam").first():
                    requests.post(API, json=nam).json()
                elif db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nữ").first():
                    requests.post(API, json=nu).json()
                return response
        else:
            nhaplai(sender_id=sender_id,message=message)
    except ValueError:
        print("")


def loaido(sender_id, message, db):
    try:
        if ( str(message['text']).lower().strip() == "quần" or str(message['text']).lower().strip() == "áo") and db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nam").first():
            request_body_10 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Bạn muốn tư vấn về " + str(message['text']).lower().strip() + " đúng không"
                }
            }
            request_body_20 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Bạn có thể cho mình biết, bạn muốn tư vấn về " + str(message['text']).lower().strip() + " mặc trong mùa nào vậy ạ. Mùa Xuân, Hạ, Thu hay Đông vậy ạ."
                }
            }
            user_old = db.query(models.CaseIn).filter(
                models.CaseIn.id_fb == sender_id)
            user_old.update({"loaido": str(message['text']).lower(
            ).strip().title()}, synchronize_session=False)
            db.commit()
            response = requests.post(API, json=request_body_10).json()
            requests.post(API, json=request_body_20).json()
            return response
        elif ( str(message['text']).lower().strip() == "quần" or str(message['text']).lower().strip() == "áo" or str(message['text']).lower().strip() == "váy" ) and db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nữ").first():
            request_body_10 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Bạn muốn tư vấn về " + str(message['text']).lower().strip() + " đúng không"
                }
            }
            request_body_20 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Bạn có thể cho mình biết, bạn muốn tư vấn về " + str(message['text']).lower().strip() + " mặc trong mùa nào vậy ạ. Mùa Xuân, Hạ, Thu hay Đông vậy ạ."
                }
            }
            user_old = db.query(models.CaseIn).filter(
                models.CaseIn.id_fb == sender_id)
            user_old.update({"loaido": str(message['text']).lower(
            ).strip().title()}, synchronize_session=False)
            db.commit()
            response = requests.post(API, json=request_body_10).json()
            requests.post(API, json=request_body_20).json()
            return response
        else :
            nhaplai(sender_id=sender_id,message=message) 
    except:
        print("1")


def chonmua(sender_id, message, db):
    try :
        if str(message['text']).lower().strip() == "xuân" or str(message['text']).lower().strip() == "hạ" or str(message['text']).lower().strip() == "thu" or str(message['text']).lower().strip() == "đông":
            if not db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.age_type == "Thiếu Nhi").first() and not db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.age_type == "Cao Tuổi").first():
                request_body_10 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Bạn muốn tư vấn đồ mặc trong mùa " + str(message['text']).lower().strip() + " đúng không ạ."
                    }
                }
                request_body_20 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Bạn có thể cho mình biết, bạn muốn mặc trong dịp nào vậy ạ. Đi Du Lịch, Đi Làm, Ở Nhà hay Đi chơi dạo vậy ạ."
                    }
                }
                user_old = db.query(models.CaseIn).filter(
                    models.CaseIn.id_fb == sender_id)
                user_old.update({"mua": str(message['text']).lower(
                ).strip().title()}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_10).json()
                requests.post(API, json=request_body_20).json()
                return response
            elif db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.age_type == "Thiếu Nhi").first() or db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.age_type == "Cao Tuổi").first():
                request_body_10 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Bạn muốn tư vấn đồ mặc trong mùa " + str(message['text']).lower().strip() + " đúng không ạ."
                    }
                }
                request_body_20 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Bạn có thể cho mình biết, bạn muốn mặc trong dịp nào vậy ạ. Đi Du Lịch, Ở Nhà hay Đi chơi dạo vậy ạ."
                    }
                }
                user_old = db.query(models.CaseIn).filter(
                    models.CaseIn.id_fb == sender_id)
                user_old.update({"mua": str(message['text']).lower(
                ).strip().title()}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_10).json()
                requests.post(API, json=request_body_20).json()
                return response
        else :
            nhaplai(sender_id=sender_id, message=message)
    except:
        print("0")

def chondip(sender_id, message, db):
    try:
        if str(message['text']).lower().strip() == "đi du lịch" or str(message['text']).lower().strip() == "đi làm" or str(message['text']).lower().strip() == "ở nhà" or str(message['text']).lower().strip() == "đi chơi dạo":
            request_body_10 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Bạn muốn tư vấn đồ mặc " + str(message['text']).lower().strip() + " đúng không ạ"
                }
            }
            user_old = db.query(models.CaseIn).filter(
                models.CaseIn.id_fb == sender_id)
            user_old.update({"dip": str(message['text']).lower(
            ).strip().title()}, synchronize_session=False)
            db.commit()
            response = requests.post(API, json=request_body_10).json()
            if db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nữ",models.CaseIn.age_type== "Thanh-Thiếu Niên").first() or db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nữ",models.CaseIn.age_type == "Trung niên").first() :
                request_body_1 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Bạn muốn tư vấn đồ mặc theo phong cách gì vậy ạ. Thanh Lịch, Nữ Tính , Cá Tính hay Thể Thao vậy ạ."
                }
                }
                requests.post(API, json=request_body_1).json()
            elif db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.age_type == "Thiếu Nhi").first() :
                request_body_1 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Cho mình hỏi da bạn có nhạy cảm không ạ. (Bạn vui lòng trả lời Có hoặc Không giúp mình ạ)"
                }
                }
                requests.post(API, json=request_body_1).json()
            elif db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.age_type == "Cao Tuổi").first() :
                request_body_1 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Cho mình hỏi da bạn có bệnh mãn tính thường gặp nào không ạ.Xương Khớp, Mề Đay hay Không có bệnh nào đáng lo ạ."
                }
                }
                request_body_2 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "(Bạn vui lòng nhập giúp mình Xương Khớp hoặc Mề Đay hoặc Không có bệnh nào đáng lo với ạ.) "
                }
                }
                requests.post(API, json=request_body_1).json()
                requests.post(API, json=request_body_2).json()
            #Use CBR
            elif db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.age_type == "Thanh-Thiếu Niên",models.CaseIn.gioitinh== "Nam").first() or db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.age_type == "Trung Niên",models.CaseIn.gioitinh== "Nam").first() :
                res = CBRtuvan(sender_id=sender_id,message=message,db=db)
                request_body_cbr = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Với những thông tin bạn vừa cung cấp cho mình, mình xin tư vấn cho bạn nên mặc "+ res + " ạ"
                }
                }
                a = timvai(sender_id=sender_id,message=message,db=db)
                t= a.split(",")
                
                request_body_vai = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Chúng tôi đề xuất cho bạn một số loại vải phù hợp với trang phục gợi ý  : " + a 
                }
                }
                user_old = db.query(models.CaseIn).filter(
                models.CaseIn.id_fb == sender_id)
                user_old.update({"end": 1}, synchronize_session=False)
                db.commit()
                requests.post(API, json=request_body_cbr).json()
                requests.post(API, json=request_body_vai).json()
            return response
        else :
            nhaplai(sender_id=sender_id,message=message)
    except:
        print("dip")

def chonphongcach(sender_id, message, db):
    try:
        if db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nữ",models.CaseIn.age_type== "Thanh-Thiếu Niên").first() or db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.gioitinh == "Nữ",models.CaseIn.age_type == "Trung Niên").first()  :
            if str(message['text']).lower().strip() == "thanh lịch" or str(message['text']).lower().strip() == "nữ tính" or str(message['text']).lower().strip() == "cá tính" or str(message['text']).lower().strip() == "thể thao":
                request_body_10 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Bạn muốn tư vấn đồ mặc theo phong cách " + str(message['text']).lower().strip() + " đúng không ạ."
                    }
                }
                user_old = db.query(models.CaseIn).filter(
                    models.CaseIn.id_fb == sender_id)
                user_old.update({"phongcach": str(message['text']).lower(
                ).strip().title()}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_10).json()
                # use CBR
                res = CBRtuvan(sender_id=sender_id,message=message,db=db)
                request_body_cbr = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Với những thông tin bạn vừa cung cấp cho mình, mình xin tư vấn cho bạn nên mặc "+ res + " ạ"
                }
                }
                a = timvai(sender_id=sender_id,message=message,db=db)
                t= a.split(",")
                
                request_body_vai = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Chúng tôi đề xuất cho bạn một số loại vải phù hợp với trang phục gợi ý  : " + a 
                }
                }
                CBR
                requests.post(API, json=request_body_cbr).json()
                requests.post(API, json=request_body_vai).json()
                return response
            else:
                nhaplai(sender_id=sender_id,message=message)
        else:
            nhaplai(sender_id=sender_id,message=message)        
    except:
        print("0")

def chondakichung(sender_id, message, db):
    try:
        if db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.age_type == "Thiếu Nhi").first():
            if str(message['text']).lower().strip() == "có":
                request_body_10 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Da bạn bị kích ứng đúng không ạ."
                    }
                }
                user_old = db.query(models.CaseIn).filter(
                    models.CaseIn.id_fb == sender_id)
                user_old.update({"da": str(message['text']).lower(
                ).strip().title()}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_10).json()
                #use CBR
                res = CBRtuvan(sender_id=sender_id,message=message,db=db)
                request_body_cbr = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Với những thông tin bạn vừa cung cấp cho mình, mình xin tư vấn cho bạn nên mặc "+ res + " ạ"
                }
                }
                a = timvai(sender_id=sender_id,message=message,db=db)
                t= a.split(",")
                
                request_body_vai = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Chúng tôi đề xuất cho bạn một số loại vải phù hợp với trang phục gợi ý  : " + a 
                }
                }
                #CBR
                requests.post(API, json=request_body_cbr).json()
                requests.post(API, json=request_body_vai).json()
                return response
            elif str(message['text']).lower().strip() == "không":
                request_body_10 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Da bạn không bị kích ứng đúng không ạ."
                    }
                }
                user_old = db.query(models.CaseIn).filter(
                    models.CaseIn.id_fb == sender_id)
                user_old.update({"da": str(message['text']).lower(
                ).strip().title()}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_10).json()
                #CBR
                res = CBRtuvan(sender_id=sender_id,message=message,db=db)
                request_body_cbr = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Với những thông tin bạn vừa cung cấp cho mình, mình xin tư vấn cho bạn nên mặc "+ res + " ạ"
                }
                }
                a = timvai(sender_id=sender_id,message=message,db=db)
                t= a.split(",")
                
                request_body_vai = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Chúng tôi đề xuất cho bạn một số loại vải phù hợp với trang phục gợi ý  : " + a 
                }
                }
                #CBR
                requests.post(API, json=request_body_cbr).json()
                requests.post(API, json=request_body_vai).json()
                return response
            else:
                nhaplai(sender_id=sender_id,message=message)
    except:
        print("0")

def chonbenh(sender_id, message, db):
    try:
        # Xương Khớp hoặc Mề Đay hoặc Không có bệnh nào đáng lo
        if db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id, models.CaseIn.age_type == "Cao Tuổi").first():
            if str(message['text']).lower().strip() == "xương khớp":
                request_body_10 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Bạn bị bệnh " + str(message['text']).lower().strip() +  " đúng không ạ."
                    }
                }
                user_old = db.query(models.CaseIn).filter(
                    models.CaseIn.id_fb == sender_id)
                user_old.update({"da": str(message['text']).lower(
                ).strip().title()}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_10).json()
                #CBR
                res = CBRtuvan(sender_id=sender_id,message=message,db=db)
                request_body_cbr = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Với những thông tin bạn vừa cung cấp cho mình, mình xin tư vấn cho bạn nên mặc "+ res + " ạ"
                }
                }
                a = timvai(sender_id=sender_id,message=message,db=db)
                t= a.split(",")
                
                request_body_vai = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Chúng tôi đề xuất cho bạn một số loại vải phù hợp với trang phục gợi ý  : " + a 
                }
                }
                #CBR
                requests.post(API, json=request_body_cbr).json()
                requests.post(API, json=request_body_vai).json()
                return response
            elif str(message['text']).lower().strip() == "mề đay":
                request_body_10 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Bạn bị bệnh " + str(message['text']).lower().strip() +  " đúng không ạ."
                    }
                }
                
                user_old = db.query(models.CaseIn).filter(
                    models.CaseIn.id_fb == sender_id)
                user_old.update({"da": str(message['text']).lower(
                ).strip().title()}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_10).json()
                #CBR
                res = CBRtuvan(sender_id=sender_id,message=message,db=db)
                request_body_cbr = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Với những thông tin bạn vừa cung cấp cho mình, mình xin tư vấn cho bạn nên mặc "+ res + " ạ"
                }
                }
                a = timvai(sender_id=sender_id,message=message,db=db)
                t= a.split(",")
                
                request_body_vai = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Chúng tôi đề xuất cho bạn một số loại vải phù hợp với trang phục gợi ý  : " + a 
                }
                }
                #CBR
                requests.post(API, json=request_body_cbr).json()
                requests.post(API, json=request_body_vai).json()
                return response
            elif str(message['text']).lower().strip() == "không có bệnh nào đáng lo":
                request_body_10 = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": "Bạn " + str(message['text']).lower().strip() +  " đúng không ạ."
                    }
                }
               
                user_old = db.query(models.CaseIn).filter(
                    models.CaseIn.id_fb == sender_id)
                user_old.update({"da": str(message['text']).lower(
                ).strip().title()}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_10).json()
                 #CBR
                res = CBRtuvan(sender_id=sender_id,message=message,db=db)
                request_body_cbr = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Với những thông tin bạn vừa cung cấp cho mình, mình xin tư vấn cho bạn nên mặc "+ res + " ạ"
                }
                }
                a = timvai(sender_id=sender_id,message=message,db=db)
                t= a.split(",")
                
                request_body_vai = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Chúng tôi đề xuất cho bạn một số loại vải phù hợp với trang phục gợi ý  : " + a 
                }
                }
                #CBR
                requests.post(API, json=request_body_cbr).json()
                requests.post(API, json=request_body_vai).json()
                return response
            else:
                nhaplai(sender_id=sender_id,message=message)
    except:
        print("0")

def chonvai(sender_id, message, db):
    a = timvai(sender_id=sender_id,message=message,db=db)
    t= a.split(",")
    OK = checkvai(mess=str(message['text']).lower().strip(),ds=t)
    print(OK)
    try:
        if OK :
            request_body_10 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Bạn muốn chọn vải " + str(message['text']).lower().strip() +  " đúng không ạ."
                }
            }
            request_body_1 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Bạn vui lòng nhập chiều cao. ( Chiều cao vui lòng nhập đơn vị cm giúp mình với ạ, chỉ nhập phần số)"
                }
            }
            user_old = db.query(models.CaseIn).filter(
                models.CaseIn.id_fb == sender_id)
            user_old.update({"loaivai": str(message['text']).lower(
            ).strip().title()}, synchronize_session=False)
            db.commit()
            response = requests.post(API, json=request_body_10).json()
            requests.post(API, json=request_body_1).json()
            return response
        else:
            nhaplai(sender_id=sender_id,message=message)
            
    except:
        print("vai")

def nhapchieucao(sender_id, message, db):
    try:
        if str(message['text']).isdigit():
            if int(str(message['text']).lower().strip()) > 0 :
                request_body_1 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Bạn vui lòng nhập giúp mình cân nặng với ạ. ( Cân nặng được tính theo đơn vị kg, chỉ nhập phần số)."
                }
                }
                user_old = db.query(models.CaseIn).filter(
                models.CaseIn.id_fb == sender_id)
                user_old.update({"chieucao": int(str(message['text']).lower(
                ).strip())}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_1).json()
                return response
            else:
                nhaplai(sender_id=sender_id,message=message)
        else:
            nhaplai(sender_id=sender_id,message=message)
    except:
        print("0") 

def nhapcannang(sender_id, message, db):
    try:
        if str(message['text']).isdigit():
            if int(str(message['text']).lower().strip()) > 0 :
                request_body_1 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Bạn cho mình hỏi bạn thuộc tone da nào vậy ạ. Tone da ấm nóng, lạnh hay là trung tính vậy ạ."
                }
                }
                request_body_2 = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "(Bạn vui lòng nhập giúp mình: Ấm nóng, lạnh hoặc trung tính với ạ. )"
                }
                }
                user_old = db.query(models.CaseIn).filter(
                models.CaseIn.id_fb == sender_id)
                user_old.update({"cannang": int(str(message['text']).lower(
                ).strip())}, synchronize_session=False)
                db.commit()
                response = requests.post(API, json=request_body_1).json()
                requests.post(API, json=request_body_2).json()
                return response
            else:
                nhaplai(sender_id=sender_id,message=message)
    except:
        print("0") 

def chontoneda(sender_id, message, db):
    try:
        if str(message['text']).lower().strip() == "ấm nóng" or str(message['text']).lower().strip() == "lạnh" or str(message['text']).lower().strip() == "trung tính":
            request_body_1 = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "Tone da của bạn là : " + str(message['text']).lower().strip() + " đúng không ạ."
            }
            }
            user_old = db.query(models.CaseIn).filter(
            models.CaseIn.id_fb == sender_id)
            user_old.update({"mauda": str(message['text']).lower(
            ).strip().title()}, synchronize_session=False)
            db.commit()
            response = requests.post(API, json=request_body_1).json()
            final(sender_id=sender_id,message=message,db=db)
            return response
        else:
            nhaplai(sender_id=sender_id,message=message)
    except:
        print("0") 

def final(sender_id, message, db):
    user = db.query(models.CaseIn).filter(
                models.CaseIn.id_fb == sender_id).first()
    ds = CBRtuvan(sender_id=sender_id,message=message,db=db)
    qa = ds.split(",")
    print(ds)
    print(qa)
    tenvai = user.loaivai
    print(tenvai)
    OK = False
    tendo = ""
    for i in qa :
        quanao = db.query(models.QuanAo).filter(models.QuanAo.ten == i.lower().strip() ).first()
        id_quanao = quanao.id
        vai = db.query(models.Vai).filter(models.Vai.ten == tenvai.title()).first()
        id_vai = vai.id
        if db.query(models.VaiQuanAo).filter(models.VaiQuanAo.idquanao == id_quanao, models.VaiQuanAo.idvai == id_vai ).first():
            OK = True
            tendo += i

    if user.mauda == "Ấm Nóng":
        da = "màu hồng đào, vàng, đỏ  và tránh phối đồ có màu sắc quá sậm."
    elif user.mauda == "Lạnh":
        da = "màu sáng như xanh da trời, hồng sáng."
    elif user.mauda == "Trung Tính":
        da = "màu be, màu vàng nhạt, màu xám hoặc màu xanh nhạt, không nên chọn màu quá đậm, đặc biệt là đỏ tươi hay xanh lá."

    if OK :
        request_body_final = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "Qua những thông tin bạn vừa nhập chúng tôi đề xuất cho bạn loại trang phục : " + tendo.title() + " " + tenvai.title() + ", Size " + user.size + ". Chọn những loại vải có " + da 
            }
            }
        request_body_reset = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "Để tư vấn lại, vui lòng nhập : Reset"
            }
            }
        response = requests.post(API, json=request_body_final).json()
        requests.post(API, json=request_body_reset).json()
        return response

    
def timvai(sender_id, message, db):
    ds = CBRtuvan(sender_id=sender_id,message=message,db=db)
    qa = ds.split(",")
    vai = []
    for i in qa :
        quanao = db.query(models.QuanAo).filter(models.QuanAo.ten == i.lower().strip() ).first()
        id_quanao = quanao.id
        vaiquanao = db.query(models.VaiQuanAo).filter(models.VaiQuanAo.idquanao == id_quanao).all()
        for x in vaiquanao :
            id_vai = x.idvai
            tenvai = db.query(models.Vai).filter(models.Vai.id == id_vai).first()
            vai.append(tenvai.ten)
    x = set(vai)
    y = list(x)        
    res = ""
    for i in y :
        res += i + " ,"
    return res

def checkvai(mess, ds):
    for i in ds :
        if mess == i.lower().strip():
            return True
    return False
    
def reset(sender_id, message, db):
    if str(message['text']).lower().strip() == "reset":
        user = db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id)
        user_delete = user.first()
        print(user_delete)
        if user_delete:
            user.delete(synchronize_session=False)
            db.commit()
        request_body1 = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "Bạn muốn tư vấn về quần áo hay mỹ phẩm !"
            }
        }
        request_body2 = {
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "(Bạn vui lòng nhập: Quần Áo hoặc Mỹ Phẩm)"
            }
        }
        response = requests.post(API, json=request_body1).json()
        requests.post(API, json=request_body2).json()
        return response


def nhaplai(sender_id, message):
    if str(message['text']).lower().strip() :
        request_body = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Bạn vui lòng nhập lại."
                }
            }
        response = requests.post(API, json=request_body).json()
        return response

def tinhsize(sender_id,db):
    user = db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id)
    user_f = user.first()
    size = predict(int(user_f.cannang), int(user_f.tuoi), int(user_f.chieucao))
    print(size)
    user.update({"size": size}, synchronize_session=False)
    db.commit()

def CBRtuvan(sender_id, message, db):
    # result = cbrAlgorithm("1	0	0	0	1	0	0	0	1	0	0	1	0	0	0	1	0	0	1	0	1	0	0	1	0	0	0")
    # reply = ""
    try:
        
        user = db.query(models.CaseIn).filter(models.CaseIn.id_fb == sender_id)
        user_f = user.first()
        input = ""

        #check tuoi
        if user_f.tuoi >= 6 and user_f.tuoi <= 11:
            input += "0 0 1 0 "
        elif user_f.tuoi >= 12 and user_f.tuoi <= 35:
            input += "0 1 0 0 "
        elif user_f.tuoi >= 36 and user_f.tuoi <= 60:
            input += "0 0 0 1 "
        else:
            input += "1 0 0 0 "
        
        #0 1 0 0 1 0 1 0 0 0 0 1 0 0 0 10 1 0 0 0 0 1 0 0 0 0 1 0
        #check gioi tinh
        if user_f.gioitinh == "Nam":
            input += "1 0 "
        else:
            input += "0 1 "
        
        #check mua
        if user_f.mua == "Xuân":
            input += "0 0 1 0 "
        elif user_f.mua == "Hạ":
            input += "1 0 0 0 "
        elif user_f.mua == "Thu":
            input += "0 1 0 0 "
        else:
            input += "0 0 0 1 "

        #check phong cách Thanh Lịch, Nữ Tính , Cá Tính hay Thể Thao
        if user_f.phongcach != None:
            if user_f.phongcach == "Thanh Lịch":
                input += "0 0 1 0 "
            elif user_f.phongcach == "Nữ Tính":
                input += "0 0 1 0 "
            elif user_f.phongcach == "Cá Tính":
                input += "1 0 0 0 "
            elif user_f.phongcach == "Thể Thao":
                input += "0 0 0 1 "
            else:
                input += "0 1 0 0 "
        else:
            input += "0 1 0 0 "
        

        #check da kick ung
        if user_f.da != None:
            if user_f.da == "Có":
                input += "1 0 "
            else :
                input += "0 1 "
        else:
            input += "0 1 "

        #check da xương khớp, mề đay, không có bệnh nào đáng lo
        if user_f.da != None and user_f.da != "Có" and user_f.da != "Không":
            if user_f.da == "Xương Khớp":
                input += "0 0 1 "
            elif user_f.da == "Mề Đay":
                input += "0 1 0 "
            elif user_f.da == "Không Có Bệnh Nào Đáng Lo":
                input += "1 0 0 "
        else:
            input += "1 0 0 "
        
        #check dịp Đi Du Lịch, Đi Làm, Ở Nhà hay Đi chơi dạo
        if user_f.dip != None:
            if user_f.dip == "Đi Du Lịch":
                input += "0 1 0 0 "
            elif user_f.dip == "Đi Làm":
                input += "0 0 1 0 "
            elif user_f.dip == "Ở Nhà":
                input += "0 0 0 1 "
            else:
                input += "1 0 0 0 "
        else:
            input += "0 0 1 0 "

        #check loại đồ
        if user_f.loaido != None:
            if user_f.loaido == "Áo":
                input += "0 0 6 0 "
            elif user_f.loaido == "Quần":
                input += "6 0 0 0 "
            elif user_f.loaido == "Váy":
                input += "0 6 0 0 "
            else:
                input += "0 0 0 6 "
        else:
            input += "0 0 6 0 "

        print(input)
        #0 1 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0 0 
        #0 1 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0 0
        #1 0 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 1 0 1 0 0 1 0 0 0

        # return str(input)
        result = CBR(input)
        s = list(result)
        reply = ""
        for i in s:
            reply += i
        print("ket qua : "+ reply)
        return reply

    except:
        print("0") 

