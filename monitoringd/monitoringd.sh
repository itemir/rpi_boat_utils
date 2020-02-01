#!/bin/bash
current_dir=$(dirname $0)
while true; do
  $current_dir/monitoringd.py
  sleep 5
done
