## Simple Python Script to Monitor Server Status

This script checks if a website server is up or down and logs the status with a timestamp. It's written in Python and uses the `requests` library to make HTTP requests.

### How it Works

1. **Import Libraries**: The script starts by importing the necessary Python libraries.
   - `requests` for sending HTTP requests.
   - `time` for adding a delay between checks.
   - `datetime` for getting the current date and time.

```python
import requests
import time
from datetime import datetime
```

2. **Server URL**: The URL of the server you want to check. Replace `'http://your-server.com'` with your own server's URL.

```python
server_url = 'http://your-server.com'
```

3. **Check Server Status**: A function called `get_server_status` checks if the server is up or down.
   - Sends a request to the server.
   - If it gets a 200 status code, the server is up.
   - If it can't connect, the server is down.

```python
def get_server_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        pass
    return False
```

4. **Logging to File**: The script logs the status in a file called `server_status_log.txt`.

```python
with open("server_status_log.txt", "a") as log_file:
```

5. **Main Loop**: The script runs indefinitely, checking the server status every 60 seconds.
   - Calls `get_server_status` to check the server.
   - Writes the status and the current time to the log file.
   - Waits for 60 seconds before checking again.

```python
    while True:
        is_server_up = get_server_status(server_url)
        
        current_time = datetime.now()
        log_entry = f"{current_time}: {'Up' if is_server_up else 'Down'}\n"
        
        print(log_entry.strip())  # Also print to console
        log_file.write(log_entry)  # Write to log file
        
        log_file.flush()  # Ensure data is written to disk
        
        time.sleep(60)  # Check every 60 seconds
```

### Summary

This script will keep running and checking if the server at `http://your-server.com` is up or down. It logs this information in a file so you can see when (and if) your server goes offline.

