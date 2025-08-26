# VerilogHDL-Automation
Automation Python file &amp; exe for RTL Engineer
# 1. Verilog Module Instantiator ⚙️

Verilog 모듈 정의 코드를 붙여넣기만 하면, 복잡한 인스턴스화(instantiation) 코드를 자동으로 생성해주는 간단한 파이썬 스크립트입니다. 반복적인 수작업을 줄이고 휴먼 에러를 방지하여 Verilog 설계 효율을 높여줍니다.

이 스크립트는 터미널에서 바로 실행하거나, `PyInstaller`를 이용해 독립적인 Windows 실행 파일(`.exe`)로 만들어 사용할 수 있습니다.

## ✨ 주요 기능

* **모듈 자동 분석**: Verilog `module` 정의 구문을 분석하여 포트 이름, 방향(input/output), 벡터 크기(`[7:0]` 등)를 자동으로 추출합니다.
* **두 가지 연결 모드**:
    1.  **직접 입력 모드**: 각 포트에 연결할 `wire`/`reg` 이름을 사용자가 직접 입력합니다.
    2.  **자동 생성 모드**: 포트 이름 앞에 `w_` 접두사를 붙여 연결할 `wire` 이름을 자동으로 생성합니다.
* **`wire` 선언 자동 생성**: 인스턴스화에 필요한 `wire` 선언 코드를 자동으로 생성하여 코드 상단에 배치합니다.
* **깔끔한 코드 정렬**: 가독성을 높이기 위해 `wire` 선언부와 포트 연결부의 코드를 자동으로 정렬합니다.
* **반복 실행 지원**: 한 번의 작업이 끝나도 프로그램이 종료되지 않고, 사용자가 원할 때까지 계속해서 새로운 코드를 생성할 수 있습니다.

---

## 🚀 사용 방법

### 1. 파이썬 스크립트로 직접 실행

**사전 준비**: PC에 **Python 3**가 설치되어 있어야 합니다.

1.  이 리포지토리를 클론하거나 `instance.py` 파일을 다운로드합니다.
2.  터미널(CMD, PowerShell 등)을 열고 스크립트가 있는 폴더로 이동합니다.
3.  아래 명령어를 입력하여 스크립트를 실행합니다.
    ```bash
    python instance.py
    ```
4.  화면에 나타나는 안내에 따라 Verilog 모듈 코드를 붙여넣고, 모드를 선택한 뒤 필요한 정보를 입력합니다.

### 2. Windows 실행 파일 (.exe)로 실행

1.  `dist` 폴더에 있는 `instance.exe` 파일을 다운로드합니다.
2.  파일을 더블클릭하여 실행합니다.
3.  파이썬 스크립트와 동일하게 화면 안내에 따라 진행합니다.

---

## 🔧 소스 코드로 .exe 빌드하기

직접 소스 코드를 수정하고 `.exe` 파일을 만들고 싶다면 아래 단계를 따르세요.

1.  **PyInstaller 설치**
    ```bash
    pip install pyinstaller
    ```

2.  **빌드 명령어 실행**
    스크립트가 있는 폴더에서 아래 명령어를 실행하면 `dist` 폴더 안에 `instance.exe` 파일이 생성됩니다.
    ```bash
    pyinstaller --onefile instance.py
    ```

---

## 📝 사용 예시

1.  **프로그램 실행 후 아래와 같은 Verilog 모듈 코드를 터미널에 붙여넣습니다.**

    ```verilog
    module FIFO_Module (
        input               iClk,
        input               iRst,
        input      [7:0]    iData,
        input               iPush,
        input               iPop,
        output reg [7:0]    oData,
        output              oFull,
        output              oEmpty
    );
    ```

2.  **인스턴스 이름 (`U_FIFO_Main`)과 모드 (`2번: 자동 생성`)를 선택합니다.**

3.  **최종 결과물이 터미널에 출력됩니다.**

    ```verilog
    ==================================================
    🎉 완성된 Verilog 코드 🎉
    ==================================================
    // Wire & Reg Declarations
    wire           w_iClk;
    wire           w_iRst;
    wire [7:0]     w_iData;
    wire           w_iPush;
    wire           w_iPop;
    wire [7:0]     w_oData;
    wire           w_oFull;
    wire           w_oEmpty;

    // Module Instantiation for FIFO_Module
    FIFO_Module U_FIFO_Main (
        .iClk   (w_iClk),
        .iRst   (w_iRst),
        .iData  (w_iData),
        .iPush  (w_iPush),
        .iPop   (w_iPop),
        .oData  (w_oData),
        .oFull  (w_oFull),
        .oEmpty (w_oEmpty)
    );
    --------------------------------------------------

    ✅ 작업 완료!
    새로운 코드를 생성하려면 Enter를, 프로그램을 종료하려면 'exit' 또는 'q'를 입력하세요:
    ```
