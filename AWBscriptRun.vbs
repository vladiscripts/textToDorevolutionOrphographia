Set WshShell = CreateObject("WScript.Shell")
REM WshShell.Run "php AWB_sectionsSO2DO.php",0,true
WshShell.Run "python toDOawb.py",0,true