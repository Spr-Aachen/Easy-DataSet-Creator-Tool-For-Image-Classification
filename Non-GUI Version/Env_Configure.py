import os


def PIPCheck():
    os.system("python -m pip --default-timeout=900 install --upgrade pip")

def PackageInstall():
    libs = {"numpy", "pandas", "matplotlib", "requests", "tqdm", "opencv-python"}
    for lib in libs:
        os.system("pip install -i https://pypi.mirrors.ustc.edu.cn/simple " + lib)