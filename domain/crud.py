# 각각의 domain에서 수행하는 역할을 함수로 만들어둔다.
# router에서 사용된다.

from models import Records
from sqlalchemy.orm import Session

# 모든 기록을 반환하는 함수 -> 첫 화면에서 사용됨
def get_records(db:Session):
    records = db.query(Records).order_by(Records.id.desc()).all()