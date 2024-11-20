プロジェクトドキュメント: ESP32 OTA & シリアルアップローダー

ESP32 OTA & シリアルアップローダー
このプロジェクトは、ESP32ファームウェアをOTA（Over-The-Air）およびシリアルアップロードで更新するためのGUIツールを提供します。
ツールは使いやすさを考慮して設計されており、ファームウェアファイルの選択、デバイスIPアドレスの指定、
コマンドライン操作なしでアップロードを実行できます。

依存関係
このプロジェクトには以下のPythonライブラリとツールが必要です：

1. tkinter: GUI開発用（Python標準ライブラリ）。
2. serial.tools.list_ports: シリアルポートリスト取得用（pyserialの一部）。
3. threading: マルチスレッドサポート（Python標準ライブラリ）。
4. subprocess: 外部コマンドの実行用（Python標準ライブラリ）。
5. osとsys: ファイル操作およびシステムアクセス用（Python標準ライブラリ）。

また、以下の外部ツールを使用します：
- esptool: ESP32デバイスへのファームウェア書き込み用コマンドラインユーティリティ。
- espota.py: OTAファームウェアアップデート用スクリプト。

インストールガイド

手順1: Python仮想環境を作成
プロジェクトディレクトリ内で以下のコマンドを実行します：
```
python -m venv .
```

手順2: 仮想環境を有効化
Windows PowerShellの場合：
```
.\Scripts\Activate.ps1
```
Linux/MacOSの場合：
```
source ./bin/activate
```

手順3: 必要なPythonライブラリをインストール
以下のコマンドを実行して依存関係をインストールします：
```
pip install pyserial
```

手順4: esptoolのインストール
以下のコマンドを使用してesptoolをインストールします：

コードをコピーする
pip install esptool

手順5: インストール確認
以下のコマンドでインストール済みライブラリを確認します：

コードをコピーする
pip list

使用方法

1. アプリケーションを実行します：
```
python OTA UploadTool.py
```
2. OTAまたはシリアルアップロード用のファームウェアファイル(.bin)を選択します。
3. OTAの場合：
   - ESP32のIPアドレスを入力します。
   - 「OTA Update」をクリックしてアップロードを開始します。
4. シリアルの場合：
   - ブートローダー、パーティション、ファームウェアファイルを選択します。
   - COMポートとボーレートを選択します。
   - 「Serial Update」をクリックしてアップロードを開始します。

ライセンス情報

プロジェクトにはPython標準ライブラリおよび外部ツールが含まれています。各コンポーネントのライセンス情報は以下の通りです：

Pythonライブラリ
- tkinter、threading、subprocess、os、sys：Python Software Foundation Licenseの下でライセンスされています。

外部ツール
1. pyserial: BSD License。
2. esptool: GPLv2 License。
3. espota.py: Apache License 2.0。

詳細はプロジェクトのLICENSEファイルを参照してください。



Project Documentation: ESP32 OTA & Serial Uploader
ESP32 OTA & Serial Uploader
This project provides a GUI tool for updating ESP32 firmware via OTA (Over-The-Air) and serial
upload methods.
The tool is designed for convenience and ease of use, allowing users to select firmware files, specify
device IP addresses,
and perform uploads without manual command-line interaction.
Dependencies
## Dependencies
This project requires the following Python libraries and tools:
1. `tkinter`: For GUI development (Python Standard Library).
2. `serial.tools.list_ports`: For listing serial ports (part of pyserial).
3. `threading`: For multithreading support (Python Standard Library).
4. `subprocess`: For executing external commands (Python Standard Library).
5. `os` and `sys`: For file operations and system-level access (Python Standard Library).
Additionally, the following external tools are used:
- `esptool`: A command-line utility for flashing firmware to ESP32 devices.
- `espota.py`: A script for performing OTA firmware updates.
Installation Guide
## Installation Guide
### Step 1: Create a Python Virtual Environment
Run the following command to create a new virtual environment in the project directory:

Project Documentation: ESP32 OTA & Serial Uploader
```
python -m venv .
```
### Step 2: Activate the Virtual Environment
For Windows PowerShell:
```
.\Scripts\Activate.ps1
```
For Linux/MacOS:
```
source ./bin/activate
```
### Step 3: Install Required Python Libraries
Run the following command to install dependencies:
```
pip install pyserial
```
### Step 4: Verify Installation
Ensure that all libraries are installed correctly by running:
```
pip list
```

Project Documentation: ESP32 OTA & Serial Uploader
Usage Instructions
## Usage Instructions
1. Run the application:
```
python OTA UploadTool.py
```
2. Select the firmware file (.bin) for OTA or serial upload.
3. For OTA:
- Enter the ESP32's IP address.
- Click "OTA Update" to initiate the upload.
4. For Serial:
- Select the bootloader, partitions, and firmware files.
- Choose the COM port and baud rate.
- Click "Serial Update" to start the upload.
License Information
## License Information
The project includes both Python Standard Libraries and external tools. Below are the licenses for
each component:
### Python Libraries
- `tkinter`, `threading`, `subprocess`, `os`, `sys`: Licensed under the Python Software Foundation
License.
Project Documentation: ESP32 OTA & Serial Uploader
### External Tools
1. `pyserial`: BSD License.
2. `esptool`: GPLv2 License.
3. `espota.py`: Apache License 2.0.
Refer to the project's LICENSE file for more details.
