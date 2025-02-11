#!/bin/bash

# Ensure data directory exists
mkdir -p data

# Capture TCP, UDP, and ARP packets separately
tcpdump -ne -c 1000 'arp' > data/arp.txt &
tcpdump -ne -c 1000 'udp' > data/udp.txt &
tcpdump -ne -c 1000 'tcp' > data/tcp.txt &

# Wait for processes to finish
wait

# Set correct permissions
chmod 755 data/*.txt

