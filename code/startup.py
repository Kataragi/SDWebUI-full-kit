import subprocess
import sys

def is_program_installed(name):
    """指定されたプログラムがインストールされているかを確認します。"""
    try:
        subprocess.check_call([name, '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def are_required_libraries_installed(libraries):
    """必要なライブラリがインストールされているかを確認します。"""
    try:
        for lib in libraries:
            subprocess.check_call([sys.executable, '-m', 'pip', 'show', lib], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    # Pythonがインストールされているか確認します。
    if not is_program_installed('python'):
        print("Python is not installed. Please install it before running this script.")
        sys.exit(1)

    # Gitがインストールされているか確認します。
    if not is_program_installed('git'):
        print("Git is not installed. Please install it before running this script.")
        sys.exit(1)

    # 必要なライブラリがインストールされているか確認します。
    required_libraries = ['pillow']
    if not are_required_libraries_installed(required_libraries):
        print(f"The required libraries {required_libraries} are not installed. Installing them...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + required_libraries)
        except subprocess.CalledProcessError:
            print("Failed to install the required libraries. Please install them manually.")
            sys.exit(1)

    # すべてが正常であれば、main.pyを実行します。
    print("All checks passed. Running main.py...")
    try:
        subprocess.check_call([sys.executable, 'main.py'])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred when executing main.py: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()