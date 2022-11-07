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
echo Would you want to run the output?(Y/N)
choice /n 

If ERRORLEVEL = 1 goto execute
If ERRORLEVEL = 0 goto end


:execute
start ..\output\main.exe
:end
exit
