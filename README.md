# ImageEncryption
2021-1 Software Engineering Team Project 
source https://nevonprojects.com/image-encryption-using-aes-algorithm/

# Problem Statement

## Introduction
기존의 주제 였던 Image encryption using AES algorithm 으로 프로젝트를 진행하기에는 프로젝트의 취지에서 좀 벗어난다는 판단이 들었다. 따라서, 팀 회의 끝에 가상의 고객을 선정한 뒤 고객의 문제상황과 그에 따른 요구사항을 도출해서 프로젝트를 해보자는 의견이 있었고, 은행이라는 가상의 고객을 대상으로 추가적인 기능을 더 구현해보기로 했다. 즉 우리의 프로젝트 주제는 원래 Image encryption using AES algorithm 이지만, 아래에 가상으로 제시한 문제 상황과 고객을 프로젝트의 문제상황과 고객이라 가정한 뒤에, 고객의 요구사항을 만족시킬 수 있는 몇 가지 기능들을 추가로 더 구현할 계획이다.

## Problem

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

## Scenario
