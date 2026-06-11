# Brute Force Simulated Attack

A Python script developed on an Azure Linux VM that repeatedly sends login attempts to a local login simulator to generate authentication activity.

## Purpose

This script was built to simulate a brute force attack log source that can be used for monitoring and investigation exercises.

## Skills Demonstrated

- Python
- HTTP request automation
- Attack simulation
- Log generation
- Security testing

## Log File

This script does not write directly to a log file itself. It generates login attempts against the login simulator at:

http://127.0.0.1:5001

Those attempts are recorded by the target application in its own log file.
