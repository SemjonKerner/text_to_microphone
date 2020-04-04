#!/bin/bash

pactl load-module module-null-sink sink_name=Virtual1
pactl load-module module-loopback sink=Virtual1
