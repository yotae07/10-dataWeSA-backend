# 10-dataWeSA-backend
# DATAUSA 클론 프로젝트

미국의 공공데이터를 시각화하여 보여주는 홈페이지

### 개발 인원 및 기간

- 개발 기간: 2020/08/01 ~ 2020/08/14
- 개발 인원: 프론트엔드 3명, 백엔드 2명

## 팀원

- 프론트엔드: 김효식 윤지영 서동찬
- 백엔드: 이홍일 이태성

## 기술 스택 및 구현 기능

### 1. 기술 스택

- Python3, Django, Mysql, Aws(EC2, RDS)

### 2. 협업 툴

- Git, Slack, Notion, Trello

### 3. 구현 기능

- **로그인**(user app)
    - JWT를 이용하여 토큰 생성
    - 인증 Decorator를 만들어 토큰을 이용하여 통신함
    - Google, Kakao API를 통해 통신후 DB에 정보를 저장하여 토큰을 만듬

- **차트**(mobility, hospital app)
    - 차트와 관련된 항목 API 구현

- **장바구니**(cart app)
    - 사용자가 선택한 상품을 한번에 결제가 진행되어서 DB에 저장한 후 바로 클라이언트에게 결제항목을 보여줌

## 프로젝트 후기

[이태성 프로젝트 후기](https://velog.io/@yotae07/2%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9B%84%EA%B8%B0)

## 프로젝트 결과물 영상

[프로젝트 결과물 영상](http://asq.kr/gSxypSJnMav2)
