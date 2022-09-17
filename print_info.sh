#!/bin/bash

cat > /mnt/c/Users/$(whoami)/info.txt << EOF
Hello, $(whoami)

time: $(date)
os: $(cat /etc/issue.net)
home directory: /mnt/c/Users/$(whoami)
memory: $(du -sh /mnt/c/Users/$(whoami)) (used), $(df -h --total | grep C:) (free)
num folders: $(cd /mnt/c/Users/$(whoami); ls -l | grep -c ^d)
num files: $(find /mnt/c/Users/$(whoami) -type f | wc -l)
EOF