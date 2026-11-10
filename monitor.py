def check_cpu(load):
    if load >= 80:
        return "CPU Overload"
    else:
        return "CPU Normal"

cpu_stats = {
    "web-prod-01": 42,
    "db-prod-01": 89,
    "api-gateway": 95,
    "worker-node": 60
}

with open("alerts.log", "a") as file:
    for server, load in cpu_stats.items():
        status = check_cpu(load)
        if status == "CPU Overload":
            log_line = f"ALERT: {server} CPU is at {load}%\n"
            file.write(log_line)
            print(f"Logged -> {log_line.strip()}")