プロジェクト ドキュメント: ESP32 OTA およびシリアル アップローダー

ESP32 OTA およびシリアル アップローダー

このプロジェクトは、OTA (Over-The-Air) およびシリアル アップロード方式で ESP32 ファームウェアを更新するための GUI ツールを提供します。

このツールは利便性と使いやすさを考慮して設計されており、ユーザーはファームウェア ファイルを選択し、デバイスの IP アドレスを指定し、手動のコマンド ライン操作なしでアップロードを実行できます。

依存関係

このプロジェクトには、次の Python ライブラリとツールが必要です:

1. tkinter: GUI 開発用 (Python 標準ライブラリ)。
2. serial.tools.list_ports: シリアル ポートの一覧表示用 (pyserial の一部)。
3. threading: マルチスレッド サポート用 (Python 標準ライブラリ)。
4. subprocess: 外部コマンドの実行用 (Python 標準ライブラリ)。
5. os および sys: ファイル操作およびシステム レベルのアクセス用 (Python 標準ライブラリ)。
   
さらに、次の外部ツールが使用されます:

- esptool: ESP32 デバイスにファームウェアをフラッシュするためのコマンド ライン ユーティリティ。
- espota.py: OTA ファームウェア更新を実行するためのスクリプト。
  
インストール ガイド

ステップ 1: Python 仮想環境を作成する

プロジェクト ディレクトリに新しい仮想環境を作成するには、次のコマンドを実行します:

python -m venv .

ステップ 2: 仮想環境をアクティブ化する

Windows PowerShell の場合:

.\Scripts\Activate.ps1

Linux/MacOS の場合:

source ./bin/activate

ステップ 3: 必要な Python ライブラリをインストールする

依存関係をインストールするには、次のコマンドを実行します:

pip install pyserial

ステップ 4: esptool をインストールする

esptool をインストールするには、次のコマンドを実行します:

pip install esptool

ステップ 5: espota.pyのビルド

pyinstaller --onefile espota.py

ステップ 6: インストールを確認する

次のコマンドを実行して、すべてのライブラリが正しくインストールされていることを確認します:

pip list

実行可能ファイルのビルド

実行可能ファイルを生成するには、次のコマンドを使用します:

pyinstaller --clean --onefile --noconsole --add-data "espota.py;." --add-data
"scripts/esptool.exe;scripts" --hidden-import serial.tools.list_ports --hidden-import
tkinter "OTA UploadTool.py"

使用方法
1. アプリケーションを実行します:
python OTA UploadTool.py
2. OTA またはシリアル アップロード用のファームウェア ファイル (.bin) を選択します。
3. OTA の場合:
- ESP32 の IP アドレスを入力します。
- [OTA 更新] をクリックしてアップロードを開始します。
4. シリアルの場合:
- ブートローダー、パーティション、ファームウェア ファイルを選択します。
- COM ポートとボー レートを選択します。
- [シリアル更新] をクリックしてアップロードを開始します。
ライセンス情報
このプロジェクトには、Python 標準ライブラリと外部ツールの両方が含まれています。各コンポーネントのライセンスは次のとおりです:
Python ライブラリ
- tkinter、threading、subprocess、os、sys: Python Software Foundation ライセンスに基づいてライセンスされています。
外部ツール
1. pyserial: BSD ライセンス。
2. esptool: GPLv2 ライセンス。
3. espota.py: Apache ライセンス 2.0。
詳細については、プロジェクトの LICENSE ファイルを参照してください。


Project Documentation: ESP32 OTA & Serial Uploader
ESP32 OTA & Serial Uploader
This project provides a GUI tool for updating ESP32 firmware via OTA (Over-The-Air) and
serial upload methods.
The tool is designed for convenience and ease of use, allowing users to select firmware
files, specify device IP addresses,
and perform uploads without manual command-line interaction.
Dependencies
This project requires the following Python libraries and tools:
1. tkinter: For GUI development (Python Standard Library).
2. serial.tools.list_ports: For listing serial ports (part of pyserial).
3. threading: For multithreading support (Python Standard Library).
4. subprocess: For executing external commands (Python Standard Library).
5. os and sys: For file operations and system-level access (Python Standard Library).
Additionally, the following external tools are used:
- esptool: A command-line utility for flashing firmware to ESP32 devices.
- espota.py: A script for performing OTA firmware updates.
Installation Guide
Step 1: Create a Python Virtual Environment
Run the following command to create a new virtual environment in the project
directory:
python -m venv .
Step 2: Activate the Virtual Environment
For Windows PowerShell:
.\Scripts\Activate.ps1
For Linux/MacOS:
source ./bin/activate
Step 3: Install Required Python Libraries
Run the following command to install dependencies:
pip install pyserial
Step 4: Install esptool
Run the following command to install esptool:
pip install esptool
Step 5: Verify Installation
Ensure that all libraries are installed correctly by running:
pip list
Building the Executable
Use the following command to generate an executable file:
pyinstaller --clean --onefile --noconsole --add-data "espota.py;." --add-data
"scripts/esptool.exe;scripts" --hidden-import serial.tools.list_ports --hidden-import
tkinter "OTA UploadTool.py"
Usage Instructions
1. Run the application:
python OTA UploadTool.py
2. Select the firmware file (.bin) for OTA or serial upload.
3. For OTA:
 - Enter the ESP32's IP address.
 - Click "OTA Update" to initiate the upload.
4. For Serial:
 - Select the bootloader, partitions, and firmware files.
 - Choose the COM port and baud rate.
 - Click "Serial Update" to start the upload.
License Information
The project includes both Python Standard Libraries and external tools. Below are the
licenses for each component:
Python Libraries
- tkinter, threading, subprocess, os, sys: Licensed under the Python Software
Foundation License.
External Tools
1. pyserial: BSD License.
2. esptool: GPLv2 License.
3. espota.py: Apache License 2.0.
Refer to the project's LICENSE file for more details.
