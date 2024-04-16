# 특정 domain에 대한 수행 역할을 부여
# crud파일의 각 함수를 실행하여 특정 기능이 수행 됨

from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session

from models import Records
from database import get_db
from domain import schema, crud

router = APIRouter(prefix='/records')

@router.get('')
def records(db: Session=Depends(get_db)):
    _records = crud.get_records(db) # crud의 함수를 통해 기록 리스트를 가져온다.
    return _records