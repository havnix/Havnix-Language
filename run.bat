@echo off
title Havnix 1.0.0 (Powered by Osman Salih)
color a
:run_program
cls
python havnix.py main.havnix
echo.
echo -----------------------
echo.
echo Press [1] to reload...
echo Press [2] to exit...
echo.
echo -----------------------
echo.
choice /c 12 /n
if errorlevel 2 goto :eof
if errorlevel 1 goto run_program
