import psutil
import time
from plyer import notification

def practice():
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()

            if cpu_usage > 0:
                notification.notify(
                    title="High CPU usage alert!",
                    message=f"CPU Usage is at {cpu_usage}%",
                    timeout=5
                )

            log_entry = "Current CPU Usage: " + str(cpu_usage) + " | Current Memory Usage: " + str(memory_info.percent)
            with open("log.txt", "a") as log_file:
                log_file.write(log_entry)

            

            print("Current CPU Usage: " + str(cpu_usage) + " | Current Memory Usage: " + str(memory_info.percent))
    except:


practice()