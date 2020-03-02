@echo off
(
set /p shebang=
) < %~dp0egybest-dl
set shebang=%shebang:#!=%
%shebang% %~dp0egybest-dl %*
