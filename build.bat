cd src
rd /s /q dist
del /q main.spec
pyinstaller --onefile -i ".\icon.ico" .\main.py
md ..\output
move /y .\dist\main.exe ..\output\
ren main.exe AmogusClck.exe
copy /y .\*.gif ..\output
copy /y .\*.wav ..\output
copy /y .\*.ico ..\output
@echo off
echo Complete
echo Would you want to run the output?(Y/N)
choice /n 
If ERRORLEVEL = 1 goto execute
If ERRORLEVEL = 0 goto end
:execute
start ..\output\main.exe
:end
exit
