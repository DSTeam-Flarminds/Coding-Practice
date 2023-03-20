import socket
import psutil
import platform

# Set the IP address of the remote machine
ip_address = "192.168.0.115"

# Create a socket object and connect to the remote machine
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip_address, 135))

# Get the system information using psutil and platform libraries

# To print memory statistics in a readable format
memory = psutil.virtual_memory()
print("Memory Information:")
print(f"Total Memory: {round(memory.total / (1024.0 ** 3), 2)} GB")
print(f"Available Memory: {round(memory.available / (1024.0 ** 3), 2)} GB")
print(f"Used Memory: {round(memory.used / (1024.0 ** 3), 2)} GB")
print(f"Memory Usage Percentage: {memory.percent}%")

# TO print CPU statistics in a readable format
cpu = psutil.cpu_percent()
print("CPU Information:")
print(f"CPU Usage: {cpu}%")

# To print disk usage statistics in a readable format
disk_usage = psutil.disk_usage('/')
print("Disk Usage Information:")
print(f"Total Disk Space: {round(disk_usage.total / (1024.0 ** 3), 2)} GB")
print(f"Used Disk Space: {round(disk_usage.used / (1024.0 ** 3), 2)} GB")
print(f"Free Disk Space: {round(disk_usage.free / (1024.0 ** 3), 2)} GB")
print(f"Disk Usage Percentage: {disk_usage.percent}%")

os_info = platform.system() + ' ' + platform.release()

# Print the system information
print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_usage}%")
print(f"Disk Usage: {disk_usage}%")
print(f"Operating System: {os_info}")

# Close the socket connection so that connection terminates
sock.close()
