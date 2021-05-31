![IEP](https://user-images.githubusercontent.com/62539910/120147757-2330a800-c222-11eb-9364-50c0de6cf496.jpg)


# ImageEncryption
2021-1 Software Engineering Team Project 
source https://nevonprojects.com/image-encryption-using-aes-algorithm/

Team Notion
https://www.notion.so/e7b05fcf792b4be9a13e5264cabe0323

# Team Info
|  이름        |     학번      |     학과    |
| ------------- |:-------------:| :-----:|
| 김영빈      | 20165079 | 산업보안학과 |
| 정도현     | 20173745      |   산업보안학과 |
| 장영욱 | 20172872      |    산업보안학과 |
| 방수원 | 20172446      |    국어국문학과 |
| 임혜정 | 20185122      |    소프트웨어학부 |
| 박희수 | 20186485      |    소프트웨어학부 |

# Problem Statement

## Introduction
기존의 주제 였던 Image encryption using AES algorithm 으로 프로젝트를 진행하기에는 프로젝트의 취지에서 좀 벗어난다는 판단이 들었다. 따라서, 팀 회의 끝에 가상의 고객을 선정한 뒤 고객의 문제상황과 그에 따른 요구사항을 도출해서 프로젝트를 해보자는 의견이 있었고, 은행이라는 가상의 고객을 대상으로 추가적인 기능을 더 구현해보기로 했다. 즉 우리의 프로젝트 주제는 원래 Image encryption using AES algorithm 이지만, 아래에 가상으로 제시한 문제 상황과 고객을 프로젝트의 문제상황과 고객이라 가정한 뒤에, 고객의 요구사항을 만족시킬 수 있는 몇 가지 기능들을 추가로 더 구현할 계획이다.

## Problem
코로나 팬더믹 사태로 사람들은 언텍트 시대에 적응하고 있고 은행 역시 비대면 계좌 계설 등 대다수의 업무를 전화 및 온라인으로 처리하고 있다. 젊은 세대부터 X세대까지 모두 코로나를 겪으면서 모든 세대가 그러한 언택트 환경을 경험하고 있다. 중요한 것은 은행 관련 업무를 온라인에서 처리하기 위해서는 신원 식별이 필수 불가결 하다는 점이다. 그러므로 은행에서는 은행 업무를 진행할 때 고객의 신원을 확인하기 위한 정보를 종종 요청하곤 한다. 법인이나 몇몇 개인들은 팩스를 통해서 서류를 전송 하기도 하지만, 대부분의 사람들의 집에는 팩스가 없다. 이런 상황에서, 중요한 문서를 사진으로 전송하면 개인정보 유출이나 보안사고가 발생할 수 있는 위험이 존재한다. 따라서 우리는 개인정보를 사진으로 보낼 때 안전하게 전송할 수 있는 플랫폼을 구축해달라는 요청을 받았고, 사용자가 전송한 사진을 은행으로 안전하게 전송하는 웹 플랫폼을 만들 계획이다.

## Method
### 고객의 요구 사항
1. 비대면 은행 업무를 선호하는 사람들이 많아지면서, 고객의 개인정보를 사진으로 찍어서 주고 받는 일이 잦아짐
2. 이때 특별한 웹 페이지를 만들어서 사용자가 웹에서 은행으로 사진을 전송하면 그 사진이 안전하게 은행에 도착하여, 은행에서 업무에 그 사진을 사용하고 싶어함

### 선택한 방법론
- Agile 방법론

### Sub-Problems
1. 사진을 안전하게 송수신 하는 기능 -> feature/PictureHandler
2. 사용자가 은행으로 서류 사진을 전송하는 기능 -> feature/Customer
3. 은행에서 사용자가 보낸 사진을 받아서 다운받는 기능 -> feature/BankClerk

![_2021-03-25__10 59 35](https://user-images.githubusercontent.com/62539910/112854665-0922fe00-90e9-11eb-9219-d080ba0bb5a6.png)

|  **Subproblem**       |     **팀원1**      |     **팀원2**    |
| :------------- |:-------------:| :-----:|
| **Feature/PictureHandler**      | 김영빈 | 박희수 |
| **Feature/Customer**     | 임혜정      |   정도현 |
| **Feature/Clerk** | 방수원      |    장영욱 |


1. PictureHandler을 구현하는 그룹은 원본 사진의 Encryption, 암호화된 사진의 Decryption, 암호화 알고리듬의 Key 관리, 암호화된 파일의 저장 및 관리등을 구현할 계획이다.
2. Customer을 구현하는 그룹은 고객의 회원가입 및 로그인, 고객 자신에게 주어진 요청 확인, 사진을 PictureHandler에게 전송하는 기능을 구현할 계획이다. 이때 자신에게 주어진 요청이란 은행에서 사용자에게 서류를 요청할 때 할당되는 이벤트이다.
3. BankClerk를 구현하는 그룹은 고객에게 서류 요청 기능, 고객이 사진을 보냈는지 확인하는 기능, 고객의 사진을 다운로드 받는 기능을 구현할 계획이다.

## Scenario
홈페이지에 접속하면 고객과 은행원을 선택하는 버튼이 표시된다. 은행원 선택 시 은행에서 각 은행원에게 부여한 아이디와 비밀번호로 로그인할 수 있다. 은행원 계정으로 로그인을 하면, 고객의 사진 서류 요청을 관리할 수 있는 페이지가 열리고 은행원은 요청을 생성하고 조회할 수 있다. 생성된 요청은 요청페이지에서 볼 수 있으며, 사진 전송이 완료된 요청, 사진 전송이 완료되지 않은 요청 두가지 탭이 존재한다. 홈페이지에서 고객은 회원가입과 로그인을 할 수 있다. 고객 계정으로 로그인을 하면 고객은 은행에서 자신에게 할당한 요청을 조회할 수 있다. 조회된 요청을 클릭하여 은행에서 요청한 사진 정보를 upload하여 전송할 수 있다. 전송된 사진은 암호화되어 은행으로 전송된다. 은행으로 사진이 전송되면 해당 요청은 사진전송이 완료된 요청으로 분류된다.
사진전송이 완료된 후, 은행원은 요청페이지에서 완료 여부를 조회가 가능하다. 전송된 사진의 다운로드 버튼을 클릭하면 암호화된 파일을 복호화 하여 사진으로 다운로드 받을 수 있다. 또한 복호화 된 사진을 다운로드 받은 후에는 웹 페이지 DB에 저장된 암호화된 파일은 삭제된다.

## Use Case
![2nd_Draft_of_UseCase](https://user-images.githubusercontent.com/62539910/115983800-6e7de800-a5de-11eb-8532-272f65458199.png)


## Traceability Matrix For Use Case
![Untitled (7)](https://user-images.githubusercontent.com/62539910/115983801-6f167e80-a5de-11eb-803e-84c1f5c97e66.png)


## Implementation

### how to run in local
```
python manage.py runserver
```
### after run enter in local web
```
http://127.0.0.1:8000/
```

## Page Organization

- /customer
- /customer/confirm
- /customer/detail/<int:pk>
- /customer/upload/<int:pk>
- /customer/signup
- /customer/login
- /customer/logout
- /customer/success
- /clerk
- /clerk/siginup
- /clerk/login
- /clerk/logout
- /clerk/create
- /clerk/create/select/<str:customer_name>
- /clerk/rlist
- /clerk/download/<int:pk>
- /clerk/decryptor/<int:pk>
- /picturehandler/encrypt/<int:pk>
- /picturehandler/decrypt/<int:pk>
- /pincturehandler/picturedelete/<int:pk>


## Use Case

### UC1 회원가입
- /customer
로그인, 회원가입
![home1]( https://user-images.githubusercontent.com/77912619/120096294-9a543680-c165-11eb-98a6-9570cfcee139.png)

- /customer/signup
회원가입 
: username, email, password, password confirgation 을 통해 회원가입을 할 수 있다. customer 값은 True
![signup1](https://user-images.githubusercontent.com/77912619/120097120-bfe33f00-c169-11eb-87f2-eb99d9ac32ae.png)


- /clerk
회원가입 및 로그인
:Clerk가 회원가입과 로그인을 할 수 있는 홈 화면이다.
![home1](https://user-images.githubusercontent.com/78745580/120116365-c9e55c00-c1c2-11eb-96e5-e3586ff80141.png)


- /clerk/signup
회원가입 
: username, email, password, password confirgation 을 통해 회원가입을 할 수 있다. Clerk 계정이 생성된다.
![signup](https://user-images.githubusercontent.com/78745580/120116412-fd27eb00-c1c2-11eb-85e0-10a3e509124c.png)



### UC2 로그인
- /customer/login
로그인
: username, password 을 입력받아 비교하여 로그인을 실행한다.
![login 1](https://user-images.githubusercontent.com/77912619/120096387-1f3f5000-c166-11eb-8d1b-6251ab67c91d.png)


- 로그인 완료 
: 로그인이 성공하였을 경우 요청확인 or logout 을 할 수 있다
![fhome2]( https://user-images.githubusercontent.com/77912619/120096409-4ac23a80-c166-11eb-94ac-f3b990824d49.png)


- /customer/logout
로그아웃 재확인
: 로그아웃에 대한 재확인을 한다.
![logout1]( https://user-images.githubusercontent.com/77912619/120096510-df2c9d00-c166-11eb-9797-b2d1879b9c3d.png)


- /clerk/login
로그인
: username, password 을 입력받아 비교하고 Clerk인지 여부를 확인하여  Clerk계정으로만 로그인을 실행할 수 있다.
![login](https://user-images.githubusercontent.com/78745580/120116438-1af55000-c1c3-11eb-9538-84d234920488.png)

- 로그인 완료 
: 로그인이 성공하였을 경우 요청생성 및 사진 다운로드를 위해 생성된 요청을 조회 할 수 있다
![home2](https://user-images.githubusercontent.com/78745580/120116503-71fb2500-c1c3-11eb-9acf-2a81caa20dd0.png)

- /clerk/logout
로그아웃 재확인
: 로그아웃 여부를 재확인을 한다.
![logout](https://user-images.githubusercontent.com/78745580/120116539-935c1100-c1c3-11eb-8191-8f6147abd3db.png)



### UC3 요청 확인
- /customer/confirm
요청확인 알람
: check request를 누른후 해당 요청이 있을경우 알람을 받을 수 있다.
![confirm 1]( https://user-images.githubusercontent.com/77912619/120096136-b1deef80-c164-11eb-9c3c-4b25e56db240.png)
요청 확인 
: 어떤 clerk로 부터 요청을 받았는지 확인할 수 있다.
![confrim 2](https://user-images.githubusercontent.com/77912619/120096185-f4083100-c164-11eb-949d-e6794332f9bc.png)

- /customer/detail/<int:pk>
생성된 요청내용 확인
: go to request 클릭 후 clear, customer, document 에 대한 값을 받는다.
![upload 1](https://user-images.githubusercontent.com/77912619/120096219-20bc4880-c165-11eb-829b-d65eea8539f2.png)


### UC4 사진 업로드
- /customer/upload/<int:pk>
사진 업로드 
: Upload 클릭 후 파일을 선택하여 해당 사진을 업로드할 수 있다. 성공적으로 업로드를 했을 경우, uploaded 는 True 값으로 바뀐다.
![upload 1](https://user-images.githubusercontent.com/77912619/120096524-f53a5d80-c166-11eb-85d5-a8710d6b3215.png)

- /customer/success
사진 업로드 성공
: 성공적으로 업로드를 했을 경우, uploaded 는 True 값으로 바뀐다.
![upload 2]( https://user-images.githubusercontent.com/77912619/120098650-1b192f80-c172-11eb-88f1-43dab46d0484.png)



### UC5 사진 암호화 
- /picturehandler/encrypt/<int:pk>
사진 암호화 후 저장
:Clerk가 원하는 customer에 Request 를 생성하면 DB에는 다음과 같이 Request가 생성 된다. 아직 customer가 사진을 업로드 하지 않았으므로 Field는 비어있는 상태이다. 사진이 업로드 되지 않았기 때문에 Uploaded가 False이다.
![1](https://user-images.githubusercontent.com/62539910/120147961-773b8c80-c222-11eb-993b-b8d7ac8dd35c.PNG)

- Customer가 사진을 업로드하면 해당 사진파일은 내부 모듈에 의해서 AES 암호화가 진행되고 암호화된 파일 .enc 가 생성되어 저장된다. Customer가 사진을 업로드한 시점에 Uploaded는 True로 바뀌어 체크박스가 채워지고 Clerk가 사진을 다운받을 수 있도록 한다.
![2](https://user-images.githubusercontent.com/62539910/120147964-786cb980-c222-11eb-8e5f-7f48bc675d5e.PNG)


### UC6 사진 복호화
- /picturehandler/decrypt/<int:pk>
사진 복호화
: Customer가 등록한 사진이 암호화 되어 저장되어 있고 Uploaded 가 True라면 Clerk는 사진 복호화 및 다운로드를 요청할 수 있다. Clerk가 사진 복호화 및 다운로드를 요청하기 직전에는 다음과 같은 내용이 DB에 들어간다.
![3](https://user-images.githubusercontent.com/62539910/120147968-799de680-c222-11eb-81c7-1ee77f5ff695.PNG)

- /picturehandler/picturedelete/<int:pk>
복호화된 사진 삭제
: Clerk가 사진을 다운받는 즉시 해당 레코드는 DB에서 삭제해서 기록을 없앤다.
![4](https://user-images.githubusercontent.com/62539910/120147969-7acf1380-c222-11eb-8cea-42b2afdc47bd.PNG)

### UC7 요청 생성
- /clerk/create
Customer 선택
: Customer의 username을 검색하여 존재할 경우 문서 선택화면으로 이동한다. Customer이외의 계정을 대상으로 요청을 생성할 수 없다.
![selectCustomer](https://user-images.githubusercontent.com/78745580/120116672-34e36280-c1c4-11eb-8af4-27fd917b1531.png)
: 일치하는 customer가 없다면 경고창이 띄워진다.
![alert1](https://user-images.githubusercontent.com/78745580/120116700-5a706c00-c1c4-11eb-84c0-79989b2ff170.png)

- /clerk/create/select/<str:customer_name>
Document 선택
: 선택한 Customer에게 요청할 문서를 선택하여 요청을 생성한다. 문서를 선택하지 않고 생성을 완료할 수 없다.
![selectDocument](https://user-images.githubusercontent.com/78745580/120116828-f4381900-c1c4-11eb-9021-39b0a417a3a2.png)


### UC8 사진 다운로드
- /clerk/rlist
요청목록 조회 
: 생성한 요청을 조회할 수 있고 사진이 업로드 되었다면 다운로드가 활성화 된다.
![requestList](https://user-images.githubusercontent.com/78745580/120116929-a374f000-c1c5-11eb-9b19-ae29ebcbb968.png)

- /clerk/download/<int:pk>
사진 다운로드
: 업로드된 사진의 다운로드를 시도하거나 뒤로 돌아갈 수 있다.
![download1](https://user-images.githubusercontent.com/78745580/120116954-c43d4580-c1c5-11eb-93ef-3029ee284e2b.png)

- /clerk/decryptor/<int:pk>
복호화된 사진 다운로드
: 암호화된 파일로 부터 원본 사진을 얻어 다운로드 할 수 있으며 홈으로 돌아가는 즉시 해당 요청은 삭제된다.
![download2](https://user-images.githubusercontent.com/78745580/120117073-69581e00-c1c6-11eb-9a4d-d4f61a3744ba.png)

















