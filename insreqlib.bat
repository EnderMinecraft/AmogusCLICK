@echo off
pip install pyinstaller

echo Would you want to build the script now?(Y/N)
choice /n 
If ERRORLEVEL = 1 goto build
If ERRORLEVEL = 0 goto end

:end
exit

:build
call .\build.bat
