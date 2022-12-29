import os

def Remover():
    os.system('Get-ChildItem -Path . -Recurse -Filter "__MACOSX" | Remove-Item -Force')
    os.system('Test-Path -Path . -Filter "__MACOSX"')
    os.system('Get-ChildItem -Path . -Recurse -Filter ".DS_Store" | Remove-Item -Force')
    os.system('Test-Path -Path . -Filter ".DS_Store"')
    os.system('Get-ChildItem -Path . -Recurse -Filter ".ipynb_checkpoints" | Remove-Item -Force')
    os.system('Test-Path -Path . -Filter ".ipynb_checkpoints"')