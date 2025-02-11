# 명령어 정리

## `git init`
- 현재 디렉토리에 `.git` 폴더를 생성하여 새로운 GIT 저장소를 초기화

## `git clone`
- 현재 디렉토리에 원격저장소 폴더를 복제

```
git clone {remote_url}
git clone {remote_url} {directory_name}
```

## `git status`


## `git add`

## `git log`
- 커밋의 히스토리를 조회
    - option
        - `

        ## `git remote`
        - 원격저장소 관리 명령어

        - 원격저장소 추가
        ```
        git remote add {remote_name} {remote_url}
        ```

        - 원격저장소 확인
        ```
        git remote -v
        ```

        - 원격저장소 삭제
        ```
        git remote 