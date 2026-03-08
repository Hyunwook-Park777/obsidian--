# 상태 확인 스크립트
$BaseDir = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)

Write-Host "=== Latest fetch_news log (last 5 lines) ==="
Get-Content (Join-Path $BaseDir "logs\fetch_news.log") -Tail 5 -Encoding UTF8

Write-Host ""
Write-Host "=== Latest news file ==="
$latest = Get-ChildItem (Join-Path $BaseDir "news") -Filter "*.md" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if ($latest) {
    Write-Host "File: $($latest.Name) / Size: $($latest.Length) bytes"
    Write-Host "--- Content ---"
    Get-Content $latest.FullName -Encoding UTF8
} else {
    Write-Host "No news files found"
}

Write-Host ""
Write-Host "=== Latest summary file ==="
$latestSummary = Get-ChildItem (Join-Path $BaseDir "summaries") -Filter "*.md" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if ($latestSummary) {
    Write-Host "File: $($latestSummary.Name) / Size: $($latestSummary.Length) bytes"
    Write-Host "--- Content ---"
    Get-Content $latestSummary.FullName -Encoding UTF8
} else {
    Write-Host "No summary files found"
}
