# Standard Python Libraries
import ipaddress
import json
from typing import Iterator, Union
import urllib.request


def output_cidrs(
    filename: str, cidrs: Iterator[Union[ipaddress.IPv4Network, ipaddress.IPv6Network]]
):
    """Output the given CIDRs to the given file."""
    with open(filename, "w", encoding="utf-8") as out:
        for cidr in cidrs:
            out.write(f"{cidr}\n")


with urllib.request.urlopen("https://ip-ranges.amazonaws.com/ip-ranges.json") as url:
    data = json.loads(url.read().decode())
    # Print all AWS IPs
    all_aws_ips = ipaddress.collapse_addresses(
        ipaddress.ip_network(ip_prefix["ip_prefix"]) for ip_prefix in data["prefixes"]
    )
    output_cidrs("awsips.txt", all_aws_ips)

    # Print all Cloudfront IPs
    cloudfront_ips = ipaddress.collapse_addresses(
        ipaddress.ip_network(ip_prefix["ip_prefix"])
        for ip_prefix in data["prefixes"]
        if "CLOUDFRONT" in ip_prefix["service"]
    )
    output_cidrs("cloudfront.txt", cloudfront_ips)
