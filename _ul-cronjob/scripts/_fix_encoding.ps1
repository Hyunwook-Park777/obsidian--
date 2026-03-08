# UTF-8 with BOM으로 변환
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$files = Get-ChildItem -Path $ScriptDir -Filter "*.ps1" -File | Where-Object { $_.Name -ne "_fix_encoding.ps1" }

foreach ($f in $files) {
    $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    $utf8Bom = [System.Text.UTF8Encoding]::new($true)
    [System.IO.File]::WriteAllText($f.FullName, $content, $utf8Bom)
    Write-Host "Converted: $($f.Name)"
}
Write-Host "All files converted to UTF-8 with BOM."
