# Google I/O Extended 2023 Seoul 발표

> Go 언어에서의 패키지 취약성 관리와 deps.dev API를 활용하여 다른 언어에서 이를 구축하는 방법

## 들어가며

2023년 07월 29일 토요일 코엑스 4층 컨퍼런스룸에서 진행한 [Google I/O Extended 2023 Seoul](https://festa.io/events/3683) 행사의 <Go 언어에서의 패키지 취약성 관리와 deps.dev API를 활용하여 다른 언어에서 이를 구축하는 방법> 발표에 사용된 소스 코드예요.

## 발표 자료

발표 자료는 [0417taehyun/Presentation 레포지토리](https://github.com/0417taehyun/Presentation)에서 확인할 수 있어요.

## govulncheck

> Go 언어에서 패키지를 관리하는 방법과 `govulncheck` 패키지를 활용해 취약성을 탐지하는 방법을 설명할 때 사용하는 소스 코드에요.

### `.vscode` 디렉터리

[settings.json](./govulncheck/.vscode/settings.json) 파일이 존재해요. `govulncheck` 패키지를 비주얼 스튜디오 코드(Visual Studio Code)에서 사용할 수 있게 도와요.

### `hook` 디렉터리

쉘 스크립트 [pre-commit](./govulncheck/hook/pre-commit) 파일이 존재해요. Git 훅(Hook) 중 커밋 이전에 작동 시키게 할 `pre-commit` 훅 관련 스크립트예요.

### `go.mod` 파일

[go.mod](./govulncheck/go.mod) 파일은 Go 언어에서 패키지 관리를 위해 존재하는 파일이에요. 이번 발표에서는 [Gin 웹 프레임워크](https://gin-gonic.com/) 1.1.4 버전을 패키지로 사용해요.

### `go.sum` 파일

[go.sum](./govulncheck/go.sum) 파일은 Go 언어에서 개별 패키지의 해시값 관리를 위해 존재하는 파일이에요.

### `main.go` 파일

[main.go](./govulncheck/main.go) 파일은 Gin 웹 프레임워크를 사용해 간단한 엔드포인트를 만들어 둔 파일이에요.

### `Makefile` 파일

[Makefile](./govulncheck/Makefile) 파일은 `govulncheck` 패키지 관련 명령어를 애플리케이션 빌드 전에 사용할 수 있게 도와요.

## pyvulncheck

> [deps.dev API](https://docs.deps.dev/api/v3alpha/)를 활용해 Python 언어에서 패키지 취약성을 탐지하는 방법을 설명할 때 사용하는 소스 코드예요.

### `custom` 디렉터리

`custom` 디렉터리에는 대표적으로 [types.py](./pyvulncheck/custom/types.py) 파일이 있어요. 동적 타입 언어인 Python 언어에서 deps.dev API 사용 결과로 반환 받는 JSON 객체를 안정적으로 사용하기 위해 응답을 자료형으로 만든 파일이에요.

### `util` 디렉터리

`util` 디렉터리에는 Python 언어에서 패키지를 관리하는 방법 중 하나인 `requirements.txt` 텍스트 파일 내의 값을 읽기 위한 [parser.py](./pyvulncheck/util/parser.py) 파일과 실제 deps.dev API를 호출하여 결괏값을 반환하는 [pyvulncheck.py](./pyvulncheck/util/pyvulncheck.py) 파일이 존재해요.

### `main.py` 파일은

`main.py` 파일은 패키지 정보를 조회한 뒤 API를 통해 취약성을 탐지하고 결과를 알려주는 뷰(View) 역할의 파일이에요.

### `requirements.txt` 파일

[requirements.txt](./pyvulncheck/requirements.txt) 텍스트 파일은 `go.mod` 파일처럼 패키지 관리를 위해 존재하는 파일이에요.

