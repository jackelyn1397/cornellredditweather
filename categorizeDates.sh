#!/bin/sh

chmod a+x condition.py
python ./condition.py > condition_top.txt
chmod a+x temperature.py
python ./temperature.py > temperature_top.txt