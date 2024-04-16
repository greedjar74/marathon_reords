# db에서 데이터를 가져올 때 각각의 데이터에 대한 형식을 지정해준다.
# 가져오는 데이터가 해당 형식을 잘 갖추고 있는지 검사

import datetime

from fastapi import APIRouter, Depends # Depends를 통해 db 의존성 부여
from sqlalchemy.orm import Session
from pydantic import BaseModel

from models import Records
from database import get_db

from domain import schema, crud

class record(BaseModel):
    id: int
    marathon: str
    date: datetime.date
    bib_num: int
    record: str
    dnf: bool

    # 버전에 따라 해당 부분이 없으면 오류가 발생
    class Config:
        orm_mode = True