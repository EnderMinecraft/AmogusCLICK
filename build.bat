cd src
rd /s /q dist
del /q main.spec
pyinstaller -w --onefile -i ".\icon.ico" .\main.pyw
md ..\output
move /y .\dist\main.exe ..\output\
copy /y .\*.gif ..\output
copy /y .\*.wav ..\output
copy /y .\*.ico ..\output
@echo off
echo Complete
