import os
import subprocess
import urllib.request
import winreg
import sys

def is_python_installed():
    """Pythonがインストールされているかを確認します。"""
    try:
        # Pythonのバージョンを取得
        output = subprocess.check_output(["python", "--version"], stderr=subprocess.STDOUT)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def download_python(download_path):
    """指定されたURLからPythonをダウンロードします。"""
    python_url = "https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe"
    python_installer = os.path.join(download_path, "python-3.10.6-amd64.exe")
    
    print("Pythonをダウンロードしています...")
    urllib.request.urlretrieve(python_url, python_installer)
    print("Pythonのダウンロードが完了しました。")
    return python_installer

def install_python(python_installer):
    """Pythonがインストールされていない場合、インストールを行います。"""
    if not is_python_installed():
        print("Pythonがインストールされていません。インストールを開始します。")
        
        print("Pythonをインストールしています...")
        subprocess.run([python_installer, "/quiet", "PrependPath=1"], check=True)
        print("Pythonのインストールが完了しました。")
    else:
        print("Pythonはすでにインストールされています。")

def is_git_installed():
    """Gitがインストールされているかを確認します。"""
    try:
        # Gitのバージョンを取得
        output = subprocess.check_output(["git", "--version"], stderr=subprocess.STDOUT)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def download_git(download_path):
    """指定されたURLからGitをダウンロードします。"""
    git_url = "https://github.com/git-for-windows/git/releases/download/v2.44.0.windows.1/Git-2.44.0-64-bit.exe"
    git_installer = os.path.join(download_path, "Git-2.44.0-64-bit.exe")
    
    print("Gitをダウンロードしています...")
    urllib.request.urlretrieve(git_url, git_installer)
    print("Gitのダウンロードが完了しました。")
    return git_installer

def install_git(git_installer):
    """Gitがインストールされていない場合、インストールを行います。"""
    if not is_git_installed():
        print("Gitがインストールされていません。インストールを開始します。")
        
        print("Gitをインストールしています...")
        subprocess.run([git_installer, "/VERYSILENT", "/NORESTART", "/NOCANCEL", "/SP-", "/CLOSEAPPLICATIONS", "/RESTARTAPPLICATIONS"], check=True)
        print("Gitのインストールが完了しました。")
        
        # 環境変数PATHにGitのパスを追加
        git_path = r"C:\Program Files\Git\cmd"
        os.environ["PATH"] += os.pathsep + git_path
        print("環境変数PATHにGitのパスを追加しました。")
    else:
        print("Gitはすでにインストールされています。")

if __name__ == "__main__":
    download_path = "download"
    
    # "download" フォルダが存在しない場合は作成する
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    python_installer = download_python(download_path)
    git_installer = download_git(download_path)
    
    install_python(python_installer)
    install_git(git_installer)
    print("すべての操作が完了しました。")
    sys.exit(0)