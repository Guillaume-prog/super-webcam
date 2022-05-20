#!/bin/bash

sudo modprobe v4l2loopback devices=2
source venv/bin/activate
python3 src/main.py