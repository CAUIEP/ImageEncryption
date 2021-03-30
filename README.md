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
1. 사진을 안전하게 송수신 하는 기능 -> feature/Encryption
2. 사용자가 은행으로 서류 사진을 전송하는 기능 -> feature/User
3. 은행에서 사용자가 보낸 사진을 받아서 다운받는 기능 -> feature/Bank

![_2021-03-25__10 59 35](https://user-images.githubusercontent.com/62539910/112854665-0922fe00-90e9-11eb-9219-d080ba0bb5a6.png)

|  **Subproblem**       |     **팀원1**      |     **팀원2**    |
| :------------- |:-------------:| :-----:|
| **Feature/Encryption**      | 김영빈 | 박희수 |
| **Feature/User**     | 임혜정      |   정도현 |
| **Feature/Bank** | 방수원      |    장영욱 |


1. Encryption을 구현하는 그룹은 원본 사진의 Encryption, 암호화된 사진의 Decryption, 암호화 알고리듬의 Key 관리를 구현할 계획이다.
2. User을 구현하는 그룹은 고객의 회원가입 및 로그인, 고객 자신에게 주어진 요청 확인, 사진을 수신자에게 전송하는 기능을 구현할 계획이다. 이때 자신에게 주어진 요청이란 은행에서 사용자에게 서류를 요청할 때 할당되는 이벤트이다.
3. Bank를 구현하는 그룹은 고객에게 서류 요청 기능, 고객이 사진을 보냈는지 확인하는 기능, 고객의 사진을 다운로드 받는 기능을 구현할 계획이다.

## Scenario
홈페이지에 접속하면 고객과 은행원을 선택하는 버튼이 표시된다. 은행원 선택 시 은행에서 각 은행원에게 부여한 아이디와 비밀번호로 로그인할 수 있다. 은행원 계정으로 로그인을 하면, 고객의 사진 서류 요청을 관리할 수 있는 페이지가 열리고 은행원은 요청을 생성하고 조회할 수 있다. 생성된 요청은 요청페이지에서 볼 수 있으며, 사진 전송이 완료된 요청, 사진 전송이 완료되지 않은 요청 두가지 탭이 존재한다. 홈페이지에서 고객은 회원가입과 로그인을 할 수 있다. 고객 계정으로 로그인을 하면 고객은 은행에서 자신에게 할당한 요청을 조회할 수 있다. 조회된 요청을 클릭하여 은행에서 요청한 사진 정보를 upload하여 전송할 수 있다. 전송된 사진은 암호화되어 은행으로 전송된다. 은행으로 사진이 전송되면 해당 요청은 사진전송이 완료된 요청으로 분류된다.
사진전송이 완료된 후, 은행원은 요청페이지에서 완료 여부를 조회가 가능하다. 전송된 사진의 다운로드 버튼을 클릭하면 암호화된 파일을 복호화 하여 사진으로 다운로드 받을 수 있다. 또한 복호화 된 사진을 다운로드 받은 후에는 웹 페이지 DB에 저장된 암호화된 파일은 삭제된다.