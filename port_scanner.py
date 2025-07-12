import socket
import sys
import time
import threading

usage = "Usage: python3 port_scanner.py TARGET START_PORT END_PORT"

print("-" * 70)
print("Python Simple Port Scanner")
print("-" * 70)

# Check arguments
if len(sys.argv) != 4:
    print(usage)
    sys.exit()

# Resolve target
try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

# Ports from command-line arguments
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print(f"Scanning target: {target}\n")

# Port scan function
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    conn = s.connect_ex((target, port))
    if conn == 0:
        print(f"[+] Port {port} is OPEN")
    s.close()

# List to store threads
threads = []

# Start scanning with threads
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("\nScanning complete.")
