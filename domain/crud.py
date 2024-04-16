# 각각의 domain에서 수행하는 역할을 함수로 만들어둔다.
# router에서 사용된다.

from datetime import datetime

from models import Records
from sqlalchemy.orm import Session
from domain import schema

# 모든 기록을 반환하는 함수 -> 첫 화면에서 사용됨
def get_records(db:Session):
    records = db.query(Records).order_by(Records.id.desc()).all()
    return records

# 기록은 db에 추가하는 함수
# new_record 형태 : '대회명_일시_배번호_기록_완주여부'
def update_record(db:Session, new_record):
    tmp = new_record.split('_') # 각 객체를 분리한다.

    marathon = tmp[0] # 
    date = tmp[1] # 문자열 형태에서 date타입으로 변환
    bibnum = int(tmp[2])
    record = tmp[3]
    dnf = bool(tmp[4])

    record = Records(marathon=marathon, date=date, bibnum=bibnum, record=record, dnf=dnf)
    db.add(record)
    db.commit()


# db에 있는 데이터 수정
# new_record 형태 : 'id_col_변환값'
def modify_record(db:Session, new_record):
    tmp = new_record.split('_')
    print(tmp)
    id = tmp[0]
    col = tmp[1]
    data = tmp[2]

    q = db.query(Records).get(id)
    # 각 col에 맞게 데이터를 정제하여 입력
    if col == 'date':
        q.date = data
    elif col == 'bibnum':
        data = int(data)
        q.bib_num = data
    elif col == 'dnf':
        data = bool(data)
        q.dnf = data
    elif col == 'marathon':
        q.marathon = data
    else :
        q.record = data

    db.commit()

# db의 특정 row삭제
def delete_record(db:Session, id):
    id = int(id)
    q = db.query(Records).get(id)
    db.delete(q)
    db.commit()