#!/bin/sh

chmod a+x condition.py
python ./condition.py > condition.txt
chmod a+x temperature.py
python ./temperature.py > temperature.txt