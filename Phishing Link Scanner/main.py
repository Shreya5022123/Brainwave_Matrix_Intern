from flask import Flask, render_template, request
import re

app = Flask(__name__)

# List of common phishing domains
phishing_urls = ["faceb00k.com", "spam.com", "g00gle.com"]

# Suspicious keywords to check
suspicious_keywords = ["login", "verify", "secure", "update", "bank"]

# Trusted domains (example)
trusted_domains = [".com", ".org", ".net", ".gov", ".edu"]

# Function to check if the URL contains an IP address
def is_ip_address(domain):
    ip_pattern = re.compile(r"(\d{1,3}\.){3}\d{1,3}")
    return bool(ip_pattern.match(domain))

# Function to check if suspicious keywords exist in the URL
def has_suspicious_keywords(link):
    return any(keyword in link for keyword in suspicious_keywords)

# Function to check if domain is in the trusted domain list
def is_trusted_domain(domain):
    return any(domain.endswith(tld) for tld in trusted_domains)

# Function to extract domain using split() method
def extract_domain(link):
    domain = link.split("//")[-1].split("/")[0]
    if domain.startswith("www."):
        domain = domain[4:]  # Remove 'www.' prefix if present
    return domain

@app.route('/', methods=["GET", "POST"])
def index():
    result = None
    link = None
    checks = {}
    
    if request.method == 'POST':
        link = request.form['link']
        
        # Extract domain from the URL using split()
        domain = extract_domain(link)
        
        # Run various checks
        checks['Is phishing domain?'] = 'Yes' if domain in phishing_urls else 'No'
        checks['Contains IP address?'] = 'Yes' if is_ip_address(domain) else 'No'
        checks['Suspicious keywords?'] = 'Yes' if has_suspicious_keywords(link) else 'No'
        checks['Trusted domain?'] = 'No' if not is_trusted_domain(domain) else 'Yes'
        checks['URL length?'] = 'Suspicious' if len(link) > 100 else 'Normal'
        
        # Determine result based on checks
        result = 'Phishing' if any(value == 'Yes' for key, value in checks.items() if key != 'Trusted domain?') else 'Safe'

    return render_template('index.html', result=result, link=link, checks=checks)

if __name__ == '__main__':
    app.run(debug=True)
