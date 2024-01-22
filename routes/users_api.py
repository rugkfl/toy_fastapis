from typing import List

from beanie import PydanticObjectId
from databases.connections import Database
from fastapi import APIRouter, Depends, HTTPException, status
from models.users import User

router = APIRouter(
    tags=["Users"]
)

user_database = Database(User)


# 회원가입(post : /)
@router.post("/")
async def create_event(body: User) -> dict:
    document = await user_database.save(body)
    return {
        "message": "회원 가입을 축하드립니다."
        ,"datas": document
    }


# 로그인(get : /{id}/{pswd})
@router.get("/{id}/{pswd}", response_model=User)
async def retrieve_event(id: PydanticObjectId, pswd) -> User:
    user = await user_database.get(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 ID입니다."
        )
    if pswd != user.pswd :
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 Password입니다."
        )
    
    return user


# 회원탈퇴(delete : /{id})
@router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    user = await user_database.get(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    user = await user_database.delete(id)

    return {
        "message": "삭제가 완료되었습니다."
        ,"datas": user
    }


# option -> 회원 수정(put :/{id})
from fastapi import Request
@router.put("/{id}", response_model=User)
async def update_event_withjson(id: PydanticObjectId, request:Request) -> User:
    user = await user_database.get(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    body = await request.json()
    updated_user = await user_database.update_withjson(id, body)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with supplied ID does not exist"
        )
    return updated_user