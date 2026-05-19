Set-Location $PSScriptRoot
# 用法: .\run.ps1 stress [major] [-voice]
$style = $args[0]
$major = if ($args.Count -ge 2 -and $args[1] -notmatch '^-') { $args[1] } else { $null }
$useVoice = $args -contains '-voice'

$cmd = "& 'C:\Users\21364\AppData\Local\Python\bin\python.exe' main.py --style $style --skip-setup"
if ($major) { $cmd += " --major '$major'" }
if (-not $useVoice) { $cmd += " --no-stt" }

Invoke-Expression $cmd
