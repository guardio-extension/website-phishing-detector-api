# -*- coding: utf-8 -*-

# importing required packages for this section
from urllib.parse import urlparse
import ipaddress
import re


def featureExtraction(url):
    try:
        # Parse URL
        parsed = urlparse(url)
        domain = parsed.netloc
        path = parsed.path

        # 1. Domain (simplified to length of domain as numeric feature)
        domain_length = len(domain)

        # 2. Having IP address
        try:
            ipaddress.ip_address(domain)
            have_ip = 1
        except:
            have_ip = 0

        # 3. Having @ symbol
        have_at = 1 if "@" in url else 0

        # 4. URL Length
        url_length = len(url)

        # 5. URL Depth
        url_depth = len([x for x in path.split("/") if x != ""])

        # 6. Redirection
        redirection = 1 if "//" in path else 0

        # 7. HTTPS in domain
        https_domain = 1 if "https" in domain else 0

        # 8. TinyURL
        tiny_url = 1 if "tinyurl" in domain or "bit.ly" in domain else 0

        # 9. Prefix or Suffix in Domain
        prefix_suffix = 1 if "-" in domain else 0

        features = [
            domain_length,
            have_ip,
            have_at,
            url_length,
            url_depth,
            redirection,
            https_domain,
            tiny_url,
            prefix_suffix,
        ]

        return features

    except Exception as e:
        print(f"Error extracting features: {str(e)}")
        return None


# converting the list to dataframe
feature_names = [
    "Domain",
    "Have_IP",
    "Have_At",
    "URL_Length",
    "URL_Depth",
    "Redirection",
    "https_Domain",
    "TinyURL",
    "Prefix/Suffix",
]
