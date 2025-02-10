# 리눅스 기본 명령어

## 0. 명령어의 기본형식
'''
command [option] [arguments]
'''

- command: 실행할 명령어, 프로그램
- options: 명령어의 옵션
- arguments: 명령어에 전달할 인자

## 1. 파일 및 디렉토리 관리

### ls (list)
- 디렉토리 내용 목록을 보여줍니다.
- options:
    - `-l`: 파일의 상세 정보 표시
    - `-a`: 숨김 파일 표시

    ### cd (change directory)
    - 현재 작업 디렉토리를 변경합니다.
    - `cd {target-directory}`
    - target-directory는 자동완성 기능을 활용 (TAB)

    ### pwd (print working directory)
    - 현재 작업 중인 디렉토리의 전체 경로를 출력

    ### mkdir (make directory)
    - 새로운 디렉토리를 생성
    - `mkdir {directory-name}`

    ### touch
    - 새로운 파일을 생성
    - 'touch {file-name}

    ### rm (remove)
    - 파일이나 폴더를 삭제
    - options
        - `-r`: 디렉토리와 그 내용을 재귀적으로 삭제

        ### cat (concatenate)
        - 파일의 내용을 출력