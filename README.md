# Cloud Server Health Monitor

A lightweight Python CLI utility that simulates real-time server CPU telemetry monitoring, evaluates node health against a user-defined threshold, and appends critical alerts to a persistent log file.

## Features
- **Dynamic Threshold Input:** Prompts the operator for a custom CPU alert threshold via CLI with `ValueError` exception handling.
- **Automated Node Evaluation:** Iterates across simulated production infrastructure (`web-prod-01`, `db-prod-01`, `api-gateway`, `worker-node`) using modular helper functions.
- **Persistent Alert Logging:** Appends breached thresholds to `alerts.log` without overwriting historical incident records.
- **Clean Repository Hygiene:** Excludes local runtime logs from version control via `.gitignore`.

## Prerequisites
- Python 3.x

## How to Run
```bash
git clone [https://github.com/yashb06/cloud-monitor.git](https://github.com/yashb06/cloud-monitor.git)
cd cloud-monitor
python3 monitor.py