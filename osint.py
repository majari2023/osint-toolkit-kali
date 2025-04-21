#!/usr/bin/env python3

import subprocess
import requests
import argparse
import os

def run_theharvester(domain):
    print(f"[+] Running theHarvester on: {domain}")
    cmd = ["theHarvester", "-d", domain, "-b", "all", "-f", "osint_results"]
    subprocess.run(cmd, stdout=subprocess.DEVNULL)
    print("[+] Results saved to osint_results.xml / .html")

def query_emailrep(email):
    print(f"[+] Querying EmailRep for: {email}")
    try:
        response = requests.get(f"https://emailrep.io/{email}")
        if response.status_code == 200:
            data = response.json()
            print(f"    - Reputation: {data.get('reputation')}")
            print(f"    - Suspicious: {data.get('suspicious')}")
            print(f"    - Summary: {data.get('summary')}")
            return data
        else:
            print("[-] Failed to retrieve email reputation.")
            return {}
    except Exception as e:
        print(f"[-] Error querying EmailRep: {e}")
        return {}

def save_output(email_data, filename="osint_summary.txt"):
    with open(filename, "w") as f:
        f.write("=== Email Reputation ===\n")
        for key, value in email_data.items():
            f.write(f"{key}: {value}\n")
    print(f"[+] Summary written to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Simple OSINT Script for Kali Linux")
    parser.add_argument("--domain", help="Target domain for theHarvester")
    parser.add_argument("--email", help="Target email for EmailRep check")
    args = parser.parse_args()

    if args.domain:
        run_theharvester(args.domain)

    if args.email:
        email_data = query_emailrep(args.email)
        save_output(email_data)

if __name__ == "__main__":
    main()

