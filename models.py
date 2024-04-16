# DB 테이블을 만드는 것
# 테이블 이름, 객체 이름 및 객체 속성에 대한 정의

from sqlalchemy import Column, Integer, String, DateTime, Time, Boolean
from database import Base

# 테이블 생성
class Records(Base):
    __tablename__ = 'records' # 테이블 이름

    id = Column(Integer, primary_key=True) # 각 데이터에 id를 부여 -> 중복 불가
    marathon = Column(String, nullable=False) # 마라톤 대회 이름 -> nullable=False : 값이 비어있을 수 없다.
    date = Column(DateTime, nullable=False) # 대회 일시
    bib_num = Column(Integer, nullable=False) # 배번호
    record = Column(String, nullable=False) # 기록
    dnf = Column(Boolean, nullable=False) # 포기여부