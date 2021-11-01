<#Commande pour avoir tous les ports netstat -aon OU -ab #>


function Test-Port
{
       param
       (
           $Address,
           $Port
       )
       $tcpClient = new-object Net.Sockets.TcpClient
       try
       {
           $tcpClient.Connect("$Address", $Port)
           Write-Host "OK" -ForegroundColor Yellow
       }
       catch
       {
           Write-Host "KO" -ForegroundColor red
       }
       finally
       {
           $tcpClient.Dispose()
       }
}
Write-Host "=====================" -ForegroundColor Yellow
Write-Host "  TESTING HTTP & SSL  " -ForegroundColor Green
Write-Host "=====================" -ForegroundColor Yellow

Write-Host "  Port 80 :  " -ForegroundColor Green
Test-Port -Address 127.0.0.1 -Port 80
Write-Host "  Port 443 :  " -ForegroundColor Green
Test-Port -Address 127.0.0.1 -Port 443

Write-Host "=====================" -ForegroundColor Yellow
Write-Host "  TESTING UDP PORTS  " -ForegroundColor Green
Write-Host "=====================" -ForegroundColor Yellow
Write-Host "  Port 5985 :  " -ForegroundColor Green
Test-Port -Address 127.0.0.1 -Port 5985

Start-Sleep -s 15
