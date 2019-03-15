#!/usr/bin/env bash

# Use `VBoxManage list vms` to check installed virtual devices.
vm_name="a1bc47eb-3a96-4238-9fd4-5de04799942f"

if [ "$1" != "" ]; then
    vm_name=$1
fi

/Applications/Genymotion.app/Contents/MacOS/player --vm-name "$vm_name"
