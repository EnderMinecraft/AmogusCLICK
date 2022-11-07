cd src
rd /s /q dist
del /q main.spec
pyinstaller -w --onefile -i ".\icon.ico" .\main.pyw
md ..\output
move /y .\dist\main.exe ..\output\
move /y .\*.gif ..\output
move /y .\*.wav ..\output
move /y .\*.ico ..\output
@echo off
echo Complete