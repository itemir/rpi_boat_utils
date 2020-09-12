#!/bin/bash
current_dir=$(dirname $0)
while true; do
  $current_dir/sensord.py
  sleep 5
done
