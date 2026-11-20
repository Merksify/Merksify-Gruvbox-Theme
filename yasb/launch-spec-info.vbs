Set sh = CreateObject("WScript.Shell")
sh.Run "powershell.exe -NoProfile -ExecutionPolicy Bypass -File ""C:\Users\Merks\AppData\Local\YASB\spec-info.ps1""", 0, False
Set sh = Nothing
