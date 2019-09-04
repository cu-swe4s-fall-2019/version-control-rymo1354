#!/bin/bash

chmod +x run.sh

#conda.bat activate swe4s
conda activate swe4s
#activate swe4s

echo ...running calculate.py...
python calculate.py -a 3 -b 4
