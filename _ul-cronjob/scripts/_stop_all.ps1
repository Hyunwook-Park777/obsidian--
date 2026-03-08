# 모든 AI 자동화 프로세스 종료
$targets = Get-Process powershell -ErrorAction SilentlyContinue | Where-Object {
    $_.MainWindowTitle -match '\[AI\]'
}
if ($targets) {
    $targets | ForEach-Object {
        Write-Host "Stopping: $($_.MainWindowTitle) (PID: $($_.Id))"
        Stop-Process -Id $_.Id -Force
    }
    Write-Host "All AI automation processes stopped."
} else {
    Write-Host "No running AI automation processes found."
}
