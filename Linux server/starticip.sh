#!/bin/bash

# Set configuration variables
INTERFACE=""  # Change according to your network interface name
STATIC_IP=""  # Set static IP
GATEWAY=""  # Set Gateway
DNS=""  # Set DNS

# Backup the current configuration file
cp /etc/netplan/00-installer-config.yaml /etc/netplan/00-installer-config.yaml.bak

echo "Creating static IP configuration for $INTERFACE..."

# Write new configuration to the file
cat <<EOT > /etc/netplan/00-installer-config.yaml
network:
  version: 2
  ethernets:
    $INTERFACE:
      addresses:
        - $STATIC_IP
      gateway4: $GATEWAY
      nameservers:
        addresses: [$DNS]
EOT

# Apply network configuration
netplan apply

echo "Static IP configuration has been successfully applied!"
