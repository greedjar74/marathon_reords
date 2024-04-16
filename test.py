from models import Records
import datetime
from database import SessionLocal

marathon = '대구마라톤'
date = datetime.date(2024, 4, 7)
bib_num = 4670
record = '3:07:31'
dnf = False

db = SessionLocal()

q = Records(marathon=marathon, date=date, bib_num=bib_num, record=record, dnf=dnf)
db.add(q)
db.commit()