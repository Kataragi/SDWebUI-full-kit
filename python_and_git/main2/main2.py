import os
import subprocess
import urllib.request
import winreg
import sys

def install_packages():
    """必要なパッケージをインストールします。"""
    packages = [
        "requests",
        "PyQt5"
    ]
    print("パッケージのインストールを開始します...")
    
    for package in packages:
        while True:
            print(f"{package}をインストールしています...")
            pip_executable = "pip"  # pipコマンドのパスを指定
            command = [pip_executable, "install", package]
            process = subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
            process.wait()
            return_code = process.returncode
            if return_code == 0:
                print(f"{package}のインストールが完了しました。")
                break
            else:
                print(f"{package}のインストール中にエラーが発生しました。")
                choice = input("リトライしますか？ (y/n): ")
                if choice.lower() != 'y':
                    print("インストールを終了します。")
                    return
    
    print("すべてのパッケージのインストールが完了しました。")
    return

if __name__ == "__main__":
    install_packages()