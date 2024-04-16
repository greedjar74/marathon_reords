from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain import router

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# router파일을 사용
# main에 작성할 수도 있지만 코드가 복잡해질 수 있기에 따로 구성하여 관리
app.include_router(router.router)