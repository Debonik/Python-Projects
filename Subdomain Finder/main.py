import requests

def find_subdomains(domain, wordlist):
    found_subdomains = []

    for sub in wordlist:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"Found: {url}")
                found_subdomains.append(url)
        except (requests.ConnectionError, requests.Timeout):
            pass  # Do nothing if the subdomain does not respond or times out

    return found_subdomains

# Sample wordlist (you would typically load a much larger list from a file)
wordlist = ['blog', 'mail', 'dev', 'shop', 'forum', 'app', 'search']

# Replace this with the domain you have permission to test
domain = "aeccglobal.com"

# Function call
find_subdomains(domain, wordlist)
