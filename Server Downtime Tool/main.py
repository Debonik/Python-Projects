import requests
import time
from datetime import datetime

# Replace with the IP or domain you're interested in
server_url = 'http://aeccglobal.com'

def get_server_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        pass
    return False

# Open a log file to record server status
with open("server_status_log.txt", "a") as log_file:
    while True:
        is_server_up = get_server_status(server_url)
        
        current_time = datetime.now()
        log_entry = f"{current_time}: {'Up' if is_server_up else 'Down'}\n"
        
        print(log_entry.strip())  # Also print to console
        log_file.write(log_entry)  # Write to log file
        
        log_file.flush()  # Ensure data is written to disk
        
        time.sleep(60)  # Check every 60 seconds
