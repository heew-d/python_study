# python_study

### python 복습
- [파이썬 기초 복습](./python_ex)
- 자료형, 함수, 반복문 등 예시 코드 작성

### python maze
- [python 미로찾기](./MAZE_PY)

### pygame study
- [pygame 연습](./pygame_study)


### 가상환경 생성
- 가상환경 생성
```bash
$ python -m venv venv
```

- 우분투에서 파이썬3을 사용할 때
```bash
$ python3 -m venv venv
```

- 우분투에선 가상환경명령(venv) 설치
```bash
$ sudo apt-get install python3-venv
```

- 가상환경 활성화
    - 파워쉘
    ```bash
    $ ./venv/Scripts/Activate.ps1
    ```
    - CMD
    ```bash
    $ ./venv/Scripts/activate.bat
    ```
    - 윈도우10 이상 사용시 보안설정
        - 파워쉘을 관리자 권한으로 열고
        ```bash
        $ Set-ExecutionPolicy Unrestricted
        ```
    $  source ./venv/bin/activate
    ```
- 가상환경 비활성화
```bash
(가상환경이름) $ Deactivate
```

### pyside2
- 가상환경에 pyside2 설치
```bash
$ pip install pyside2
```