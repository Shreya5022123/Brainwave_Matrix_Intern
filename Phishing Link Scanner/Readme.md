# Phishing Link Scanner

## Overview

The Phishing Link Scanner is a web application developed using Flask that helps users detect potentially malicious URLs. It evaluates URLs based on several criteria to determine if they might be phishing attempts. The application checks for known phishing domains, suspicious keywords, IP addresses in URLs, and whether the domain is trusted.

## Features

- **Phishing Domain Detection**: Identifies if the domain is in a predefined list of phishing domains.
- **IP Address Detection**: Detects if the URL contains an IP address instead of a domain name.
- **Suspicious Keywords Detection**: Looks for keywords that are commonly associated with phishing attempts.
- **Trusted Domain Check**: Verifies if the domain is part of a trusted top-level domain (TLD).
- **URL Length Analysis**: Flags URLs that exceed a certain length, which could be indicative of phishing.

## Requirements

- Python 3.x
- Flask
- Basic knowledge of HTML and CSS

