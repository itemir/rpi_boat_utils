#!/bin/bash
current_dir=$(dirname $0)
while true; do
  $current_dir/counter.py
  sleep 5
done
