
#!/bin/bash

echo "Scanning system logs for errors..."
grep -i "error" /var/log/system.log | tail -n 10
