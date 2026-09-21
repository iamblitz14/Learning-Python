Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Get the exact folder path dynamically
strPath = fso.GetParentFolderName(WScript.ScriptFullName)

' Wrap the path safely in triple quotes to handle spaces seamlessly
scriptPath = """" & strPath & "\rdp_launcher.py"""

' Use pythonw (Python Windows-Windowed) to guarantee a silent, clean launch
WshShell.Run "pythonw " & scriptPath, 0, False
