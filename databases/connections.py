# --------------------------------------------------------------------
# 기본 형태
# from typing import Any, List, Optional
# from beanie import init_beanie, PydanticObjectId
# from models.users import User
# from motor.motor_asyncio import AsyncIOMotorClient
# from pydantic import BaseModel
# 변경 후 코드
# from pydantic_settings import BaseSettings
# class Settings(BaseSettings):
#     DATABASE_URL: Optional[str] = None
#     async def initialize_database(self):
#         client = AsyncIOMotorClient(self.DATABASE_URL)
#         await init_beanie(database=client.get_default_database(),
#                           document_models=[User])
# --------------------------------------------------------------------

from typing import Any, List, Optional

from beanie import init_beanie, PydanticObjectId        # PydanticObjectId는 beanie에 들어가있다.
from models.users import User
from models.events import Event
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
# 변경 후 코드
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None        # mongodb에 접속 + database 연결 + collection 작업 을 한번에 해준다.

    async def initialize_database(self):            # async는 펑션 앞에 둔다. 그리고 await는 같이 다닌다.(네트워크 신호를 맞추기 위해서 사용한다.)
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                          document_models=[User, Event])
        
    class Config:           # IP 주소를 암호화 하기위해 따로 관리한다. 파일명 : .env
        env_file = ".env"
import json        
class Database:
    # model 즉 collection
    def __init__(self, model) -> None:
        self.model = model
        pass
    
    # 전체 리스트
    async def get_all(self) :
        documents = await self.model.find_all().to_list()       # find({})
        pass
        return documents
    
    # 상세 보기
    async def get(self, id: PydanticObjectId) -> Any:           # PydanticObjectId : 몽고디비는 ID가 절대값이기 변경하면 안되기에 특이하게 변형을 해준다.
        doc = await self.model.get(id)      # find_one()        # doc값을 가지고 왔는데 있으면 받고, 만약에 아니라면 리턴한다.
        if doc:
            return doc
        return False
    
    # 저장
    async def save(self, document) -> None:
        doc = await document.create()
        return doc
    
    # 삭제
    async def delete(self, id: PydanticObjectId):
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
    
  # update with params json
    async def update_withjson(self, id: PydanticObjectId, body: json):
        doc_id = id

        # des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {**body}}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc
