### Bash Scripts Collection

A professional collection of Bash scripts for Linux/Unix system administration, monitoring, and automation tasks. This project showcases practical skills in shell scripting and foundational knowledge of DevOps practices.

---

### Project Features

This repository includes a variety of scripts organized into two tiers:

- **Basic Scripts**: Simple, single-purpose utilities for file management, system information, and everyday tasks.
    
- **Intermediate Scripts**: More complex scripts for system monitoring, automated backups, and network diagnostics, demonstrating a deeper understanding of system administration.
    

---

### Key Highlights

- **Modular and Organized Code**: The project is structured with clear, logical directories (`Basic`, `Intermediate`) and shared function files (`common_functions.sh`), promoting code reusability and maintainability.
    
- **Best Practices**: Scripts include robust error handling (`set -euo pipefail`), clear shebangs (`#!/bin/bash`), and a consistent coding style.
    
- **Configuration Management**: Scripts use external configuration files (`default.conf`) for easy customization of settings like alert thresholds.
    
- **Automation Focus**: Demonstrates the ability to create scripts for automating routine tasks like backups and system health checks, a core skill for any DevOps role.
    
- **Clear Documentation**: Each script has a header explaining its purpose, usage, and features. The README provides a comprehensive overview of the entire project.
    

---

### Installation & Usage

### Prerequisites

- **Bash 4.0+**
    
- **Standard Linux utilities** such as `grep`, `awk`, `curl`, and `tar`.
    

### Quick Start

1. **Clone the repository:**
    
    Bash
    
    ```
    git clone https://github.com/your-username/bash-scripts.git
    cd bash-scripts
    ```
    
2. **Make scripts executable:**
    
    Bash
    
    ```
    chmod +x **/*.sh
    ```
    
3. **Run a script:**
    
    Bash
    
    ```
    ./Intermediate/System_Monitoring/system_report.sh
    ./Intermediate/Backup_Recovery/backup_with_cleaning.sh
    ```
    
4. Set up automation (optional):
    
    Scripts can be easily scheduled with cron for automated execution. See the Cron Examples section below for details.
    

---

### Script Descriptions

- **System Monitoring:**
    
    - `system_report.sh`: Provides a quick overview of key system metrics (CPU, RAM, disk).
        
    - `disk_monitor.sh`: Checks disk usage and alerts if a threshold is exceeded.
        
- **Backup & Recovery:**
    
    - `automated_backup.sh`: Creates compressed, dated backups and automatically manages file rotation.
        
- **Network Tools:**
    
    - `website_checker.sh`: Checks the HTTP status of a given URL.
        

> **Note:** For a full list of scripts and their functionalities, please see the `bash-scripts/` directory. Each script contains inline documentation.

---

### Project Roadmap & Future Plans

This project is a continuous effort. Future plans include:

- **Enhanced Interactivity:** Adding support for command-line arguments and more detailed help menus.
    
- **Improved Output:** Implementing colorized output and options for exporting data in formats like JSON or CSV.
    
- **Notification Integration:** Connecting scripts with services like Slack or email for alerts.
    

---

### License

MIT License - see `LICENSE` file for details.

---

### Contact

**Your Name**

- **GitHub**: `[your-github-username]`
    
- **LinkedIn**: `[your-linkedin-profile]`
    

---
