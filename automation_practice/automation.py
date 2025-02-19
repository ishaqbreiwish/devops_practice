import psutil
import time

def log_system_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage
        memory_info = psutil.virtual_memory()  # Get memory usage
        
        log_entry = f"CPU: {cpu_usage}% | Memory: {memory_info.percent}%"
        print(log_entry)

        # Save log to file
        with open("system_log.txt", "a") as log_file:
            log_file.write(log_entry + "\n")

        # Alert if usage is high
        if cpu_usage > 80 or memory_info.percent > 80:
            print("⚠️ Warning! High CPU/Memory usage!")

        time.sleep(10)  # Wait 10 seconds before next check

log_system_usage()
