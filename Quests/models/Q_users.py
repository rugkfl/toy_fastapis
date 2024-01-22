from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

class quests(Document):
    Quiz_list : Optional[str] = None            # 문제
    Quiz_answer : Optional[str] = None          # 보기
    Answer : Optional[str] = None               # 정답
    Score : Optional[str] = None                # 점수
    
    class Settings :
        name = "quests"
  