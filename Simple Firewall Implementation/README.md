
# Simple Python Firewall

## Introduction
A simple firewall developed in Python that blocks incoming and outgoing traffic based on predefined rules. This example uses Python's `socket` library to simulate basic firewall functionality.

## How It Works
1. **Blocking Incoming Traffic**: Listens on a specific port and blocks incoming connections based on rules.
2. **Blocking Outgoing Traffic**: Blocks outgoing traffic to specific IP addresses or ports.

## Code Explanation

### Importing Required Libraries
```python
import socket
```

### Defining Firewall Rules
The rules for incoming and outgoing traffic are defined in dictionaries.
```python
incoming_rules = {'block_ports': [22, 80], 'allow_ips': ['127.0.0.1']}
outgoing_rules = {'block_ports': [25], 'block_ips': ['192.168.1.2']}
```

### Checking Incoming Traffic
The function `check_incoming_traffic` validates incoming connections based on the rules.
```python
def check_incoming_traffic(ip, port):
    if port in incoming_rules['block_ports']:
        return False
    if ip not in incoming_rules['allow_ips']:
        return False
    return True
```

### Checking Outgoing Traffic
The function `check_outgoing_traffic` validates outgoing connections based on the rules.
```python
def check_outgoing_traffic(ip, port):
    if port in outgoing_rules['block_ports']:
        return False
    if ip in outgoing_rules['block_ips']:
        return False
    return True
```

### Blocking Incoming Traffic
The function `block_incoming` listens on port 5000 and blocks or allows incoming traffic based on the rules.
```python
def block_incoming():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 5000))
    s.listen(5)
    while True:
        client, addr = s.accept()
        if check_incoming_traffic(addr[0], addr[1]):
            print(f"Allowed incoming connection from {addr}")
        else:
            print(f"Blocked incoming connection from {addr}")
            client.close()
```

## Procedure to Run and Test the Firewall

### Step 1: Save the Code
Save the provided Python code into a file, for example, `simple_firewall.py`.

### Step 2: Run the Firewall
Open the Command Prompt as an administrator and navigate to the directory where `simple_firewall.py` is saved. Run the script using:
```
python simple_firewall.py
```

### Step 3: Install and Use Telnet for Testing

#### Installing Telnet
1. Open the Control Panel.
2. Go to Programs and Features.
3. Click on "Turn Windows features on or off".
4. Check the box for "Telnet Client" and click OK.

#### Using Telnet
1. Open a new Command Prompt.
2. Type the following command to connect to the local machine on port 5000.
```
telnet localhost 5000
```
Your firewall script should output whether the connection is allowed or blocked.

## Expected Output
If the connection adheres to the rules, you will see:
```
Allowed incoming connection from ('127.0.0.1', some_random_port)
```
Otherwise, you will see:
```
Blocked incoming connection from ('127.0.0.1', some_random_port)
```
