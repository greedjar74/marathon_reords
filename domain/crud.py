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
def update_record(db:Session, new_record):
    new_record = str(new_record)
    tmp = new_record.split('_') # 각 객체를 분리한다.

    marathon = tmp[0] # 
    date = datetime.strptime(tmp[1], '%Y-%m-%d').date() # 문자열 형태에서 date타입으로 변환
    bib_num = int(tmp[2])
    record = tmp[3]
    dnf = bool(tmp[4])

    record = Records(marathon=marathon, date=date, bib_num=bib_num, record=record, dnf=dnf)
    db.add(record)
    db.commit()

# db에 있는 데이터 수정
def modify_record(db:Session, mew_record):
    pass