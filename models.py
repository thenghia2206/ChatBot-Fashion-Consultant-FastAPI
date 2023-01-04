from database import Base
from sqlalchemy import Column,Integer,Text,ForeignKey


class CaseIn(Base):
    __tablename__= "casein"
    id = Column(Integer, primary_key=True, nullable=False)
    loaituvan = Column(Text, nullable = False)
    id_fb = Column(Text,nullable=False)
    gioitinh = Column(Text)
    tuoi = Column(Integer)
    age_type = Column(Text)
    loaido = Column(Text)
    mua = Column(Text)
    dip = Column(Text)
    end = Column(Integer, default = 0)
    phongcach = Column(Text)
    da = Column(Text)
    loaivai = Column(Text)
    chieucao = Column(Integer)
    cannang = Column(Integer)
    mauda = Column(Text)
    size = Column(Text)

class QuanAo(Base):
    __tablename__= "quanao"
    id = Column(Integer, primary_key=True, nullable=False)
    ten = Column(Text)

class SanPham(Base):
    __tablename__= "sanpham"
    id = Column(Integer, primary_key=True, nullable=False)
    tensanpham = Column(Text)
    idvaiquanao = Column(Integer, ForeignKey("quanao.id"), nullable=False )

class Vai(Base):
    __tablename__= "vai"
    id = Column(Integer, primary_key=True, nullable=False)
    ten = Column(Text)

class VaiQuanAo(Base):
    __tablename__= "vaiquanao"
    id = Column(Integer, primary_key=True, nullable=False)
    idvai = Column(Integer, ForeignKey("vai.id"), nullable=False )
    idquanao = Column(Integer, ForeignKey("quanao.id"), nullable=False )



