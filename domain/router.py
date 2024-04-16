# 특정 domain에 대한 수행 역할을 부여
# crud파일의 각 함수를 실행하여 특정 기능이 수행 됨

from datetime import datetime

from fastapi import FastAPI, APIRouter, Depends # Depends를 통해 의존성 부여
from sqlalchemy.orm import Session

from models import Records
from database import get_db
from domain import schema, crud

router = APIRouter(prefix='')

# 메인 화면
@router.get('/records', response_model=list[schema.record])
def records(db: Session=Depends(get_db)):
    _records = crud.get_records(db) # crud의 함수를 통해 기록 리스트를 가져온다.
    return _records

# 특정 기록 가져오기
@router.get('/record_detail/{record_id}', response_model=schema.record)
def get_record_detail(id, db: Session=Depends(get_db)):
    _record_detail = crud.get_record_detail(db, id=id)
    return _record_detail

# 기록 입력
# 유저에게 입력을 받는다. -> post사용
# 입력 데이터 형태 : '대회명_일시_배번호_기록_dnf여부'
@router.post('/update_record')
def update_record(new_record, db: Session=Depends(get_db)): # schema를 통해 미리 설정한 데이터 형태에 부합하는지 확인
    crud.update_record(db=db,new_record=new_record)

# 기록 수정
# id를 통해 특정 데이터를 가져오고 객체를 수정한다.
# 입력 데이터 형태 : 'id_col_변환값'
@router.post('/modify_record')
def modify_record(new_record, db: Session=Depends(get_db)):
    crud.modify_record(db=db, new_record=new_record)

# 특정 기록 삭제
# id를 통해 특정 데이터를 지정하고 삭제한다.
# 입력 데이터 형태 : 'id'
@router.post('delete_record')
def delete_record(id, db: Session=Depends(get_db)):
    crud.delete_record(db=db, id=id)