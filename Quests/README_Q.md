```
~$ pip install fastapi uvicorn jinja2 beanie pydantic-settings pydantic pydantic[email]
~$ pip install python-multipart

```

### [업무분장]
|멤버|역할|
|--|--|
|김명준|문제 출제 db 업로드 및 html 담당|
|서정민|응시자 문제 풀기 python 담당|
|오지수|서버연결 및 문제풀이 참여자 리스트 python 담당|

### [파일 경로]
|파일속성|파일|설명|서버경로|
|--|--|--|--|
|python|[quests.py](routes/quests.py)|문제 풀이 전체 라우트||
|html|[create.html](templates/quests/create.html)|문제 출제|/quest/create|
|html|[test.html](templates/quests/test.html)|문제 풀이|/quest/test|
|html|[result.html](templates/quests/result.html)|결과|/quest/result|

### [컬렉션]
#### server :  mongodb:미정 (지수 mongodb 접속 불가해 정민mongodb 사용)
|num|컬렉션 이름|설명|
|--|--|--|
|1|quest_question|문제 정답 점수|
|2|quest_answer|문제id 문항|
|3|quest_user|문제id 응시자 이름. 응시자 정답, 응시자 점수|