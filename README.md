# marathon_reords

주제 : 나의 마라톤 기록을 DB에 넣어두고 웹에 접속하여 기록 확인 및 수정 등을 수행한다.

구현 기능
1. fastapi를 사용하여 backend 구성
    - 메인 : 나의 기록들을 리스트 형태로 반환
    - 디테일 : id를 통해 특정 기록을 가져오고 모든 데이터를 출력한다.
    - 입력 : 사용자로부터 기록을 입력받아 db에 저장한다.
    - 수정 : id를 통해 객체를 가져오고 특정 데이터를 수정한다.
    - 객체 삭제 : id를 통해 객체를 가져오고 해당 객체를 db에서 삭제한다.
    - 데이터 전체 삭제 : db에 저장된 모든 객체를 삭제한다.

2. DataBase 구성
    - Local : sqlite를 사용하여 db생성
    - EC2 : PostgreSQL을 사용하여 publish
    - db 형태
        - 테이블 이름 : records
        - col : marathon, date, bibnum, record, dnf

3. Frontend
    - 각각의 화면을 구성한다.

4. Publish
    - EC2를 사용하여 외부에서 접속가능하게 구현