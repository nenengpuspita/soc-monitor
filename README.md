# SOC Log Monitoring with Alert System

> Status : Beginners learning Python and Cybersecurity
> My first project to understand log monitoring and alert system.

## About This Project

This is my first project. It's simple, but I'm proud to have built it from the scratch.This project reads server log files, detects brute-force attacks, then provide security status and alerts. 

** WARNING **

The server log file content has been simplified to make it more user-friendly for beginners. This log file content doesn't correspond to real-world server logs. The primary focus of this project is understanding the log flow of monitoring and alert systems.

## Current Features
- Reads multiple log files from the 'security_logs/' folder.
- Counts the number of INFO, WARN, and ERROR entries.
- Detects brute-force attempts for the phrase "failed password".
- Determines the system status : NORMAL, WARNING, CRITICAL.
- Alert level : HIGH (Critical), Medium (Warning)
- Automatic reports in JSON format.

## How to Run
```bash
python3 soc_monitor.py
```
## Output Structure
- `reports/security_reports.json` -> Summary of all logs.
- `alerts/alerts.json` -> Alert if there is suspicious activity.

## RESULT OUTPUT 

**Security Report:**
```json

{
    "INFO": 5,
    "WARN": 3,
    "ERROR": 4,
    "BRUTEFORCE ATTEMPT": 5,
    "STATUS SYSTEM": "CRITICAL",
    "ALERT": "HIGH"
}
           
```

**Alert:**
```json

{
    "alert_level": "HIGH",
    "reason": "high error or brute force activity detected",
    "timestamp": "2026-02-12T16:05:26.473240Z",
    "alert_id": "b258f557-e71b-4217-ae5e-a1a34aceabaf",
    "details": {
        "ERROR": 4,
        "BRUTEFORCE ATTEMPT": 5
    }
}       

```

## What I Learned from This Project
- File manipulation in Python.
- Parsing log text.
- Dictionary and list comprehension.
- Export to JSON.
- Version control with Git & GitHub.
- GitHub authentication with Personal Access Token.

## Feedback & Discussion
I'm very open to criticism and suggestions!
Create an **issue** in this repo or contact me at nenengpuspitak57@gmail.com.

---

*Made by nenengpuspita*
*Started: 13 February 2026*

