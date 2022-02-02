#!/usr/bin/env python

# Standard Python Libraries
import json
import urllib.request

with urllib.request.urlopen("https://ip-ranges.amazonaws.com/ip-ranges.json") as url:
    data = json.loads(url.read().decode())
    # Print all AWS IPs
    allawsips = list(ip_prefix["ip_prefix"] for ip_prefix in data["prefixes"])
    with open("awsips.txt", "w") as f:
        for cidr in allawsips:
            f.write("%s\n" % cidr)
    # Print all Cloudfront IPs
    cloudfront = list(
        ip_prefix["ip_prefix"]
        for ip_prefix in data["prefixes"]
        if "CLOUDFRONT" in ip_prefix["service"]
    )
    with open("cloudfront.txt", "w") as f:
        for cidr in cloudfront:
            f.write("%s\n" % cidr)
