import socket
import sys
import threading

usage = "Usage: python3 port_scan.py TARGET START_PORT END_PORT"

print("-" * 70)
print("Python Simple Port Scanner")
print("-" * 70)

# Check arguments
if len(sys.argv) != 4:
    print(usage)
    sys.exit()

# Resolve target hostname
try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

# Get port range
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target:", target)

# Port scanning function
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()

# Start scanning with threads
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
