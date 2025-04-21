# 🕵️ OSINT Toolkit for Kali Linux

A lightweight Python-based reconnaissance tool for quickly gathering open-source intelligence (OSINT) on domains and email addresses. This tool integrates:

- 🔍 **theHarvester** — for passive domain reconnaissance  
- ✉️ **EmailRep.io API** — for reputation and threat scoring of email addresses

Ideal for cybersecurity learners, ethical hackers, or professionals needing fast insights during assessments.

---

## 📌 Features

- Collect subdomains, emails, and hostnames from a domain using theHarvester
- Query email addresses via EmailRep for:
  - Reputation (e.g., high, low, neutral)
  - Flags for suspicious or malicious behavior
  - Summary of associated data
- Save results as:
  - `osint_results.html` and `.xml` (from theHarvester)
  - `osint_summary.txt` (parsed EmailRep response)

---

## ⚙️ Requirements

- **Python 3** (tested on Python 3.8+)
- `theHarvester` (pre-installed on Kali Linux)
- Python packages:
  - `requests`

Install dependencies:
```bash
sudo apt update && sudo apt install theharvester
pip3 install requests

