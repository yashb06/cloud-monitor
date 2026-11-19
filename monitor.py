def check_cpu(load, threshold):
    if load >= threshold:
        return "CPU Overload"
    else:
        return "CPU Normal"

cpu_stats = {
    "web-prod-01": 42,
    "db-prod-01": 89,
    "api-gateway": 95,
    "worker-node": 60
}

try:
    user_threshold = int(input("Enter CPU alert threshold (e.g. 80): "))
except ValueError:
    print("Invalid input. Defaulting threshold to 80%.")
    user_threshold = 80

with open("alerts.log", "a") as file:
    for server, load in cpu_stats.items():
        status = check_cpu(load, user_threshold)
        if status == "CPU Overload":
            log_line = f"ALERT: {server} CPU is at {load}% (Threshold: {user_threshold}%)\n"
            file.write(log_line)
            print(f"Logged -> {log_line.strip()}")