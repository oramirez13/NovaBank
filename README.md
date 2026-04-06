# NovaBank - Phishing & Malware Awareness Project

> ⚠️ **EDUCATIONAL PURPOSE ONLY**
> This project is a **fictional simulation** created exclusively for academic and educational purposes.
> **NovaBank does not exist.** No real bank, brand, or institution is represented here.
> The phishing page is intentionally fake. It is designed to demonstrate how phishing attacks work — not to deceive real users.
> **Do not use any part of this project for malicious, unauthorized, or illegal activities.**

---

## 📚 Academic Context

| Field        | Detail                                      |
|--------------|---------------------------------------------|
| Author       | orami13                                     |
| Contact      | oramirezmg@gmail.com                        |
| Year         | 2024                                        |

---

## 🎯 Project Purpose

This project demonstrates the **full lifecycle of a phishing attack** from an educational perspective:

1. **The Bait** — A realistic-looking fake email alert from a fictional bank (NovaBank)
2. **Awareness** — A page explaining how phishing works and how to identify it
3. **Mitigation** — A Python script that detects and removes suspicious files and processes

The goal is to help students and general users understand phishing tactics so they can **recognize and avoid them** in real life.

---

## 🏦 About NovaBank (Fictional Entity)

**NovaBank** is a completely fictional bank created for this project.
It has no affiliation with any real financial institution.
Any resemblance to real banks, logos, or services is coincidental and unintentional.
NovaBank exists solely to simulate a realistic phishing scenario for educational demonstration.

---

## 📁 Project Structure

```
NovaBank/
│
├── index.html          # Simulated phishing page (fake NovaBank security alert)
├── blog.html           # Educational page: what is phishing and how to detect it
├── app.py              # Python script: suspicious file and process remover
│
├── css/
│   ├── style01.css     # Styles for index.html (phishing page theme)
│   └── style02.css     # Styles for blog.html (educational article theme)
│
├── js/
│   └── script.js       # Shared JavaScript (phishing warning interaction)
│
├── img/                # Project images and assets
│
└── README.md           # This file
```

---

## 🔍 How Each File Works

### `index.html` — The Phishing Simulation
A fake security alert page impersonating NovaBank.
It mimics the visual style and urgent language used in real phishing emails.
When the user clicks the download button, a JavaScript warning appears explaining that this is a phishing simulation — **the educational moment of the demo**.

### `blog.html` — The Awareness Page
An informational article explaining:
- What phishing is
- How attackers craft convincing fake pages
- Red flags to watch for in emails and websites
- How to protect yourself

### `app.py` — The Mitigation Script
A Python script that simulates malware removal by:
- Scanning a directory for files with suspicious extensions (`.exe`, `.vbs`, `.bat`, `.js`)
- Terminating known malicious process names
- Logging every action taken

---

## ▶️ How to Run `app.py`

### Requirements

```bash
pip install psutil
```

### Execution

```bash
python app.py
```

### ⚠️ Important Notes

| Note | Detail |
|------|--------|
| **Permissions** | Administrator/root privileges required to terminate processes and delete certain files |
| **OS** | Designed for Windows. Linux/macOS users must modify file paths in the script |
| **Environment** | **Always run in a virtual machine or sandbox** — never on a production system |
| **Purpose** | This script is a demonstration only. It targets fictional process names by default |

---

## 🛡️ Ethical & Legal Disclaimer

- This repository is provided **"as is"** for educational use only.
- The author does **not** encourage, endorse, or support phishing, malware distribution, or any form of cybercrime.
- All techniques shown here are well-documented in public cybersecurity literature.
- If you use materials from this repository, **give proper credit** to the original author.
- Any use outside of educational or research contexts is **strictly prohibited** and may violate local and international laws.

---

## 🔗 Related Projects

- [phishing](https://github.com/oramirez13) — Related phishing awareness demos
- [mail-1](https://github.com/oramirez13) — Email phishing simulation

---

*Thank you for using this resource responsibly.*
*— orami13*
