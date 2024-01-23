#!/bin/bash

ds=lip

python3 simple_extractor.py \
    --dataset "${ds}" \
    --model-restore "checkpoints/${ds}.pth" \
    --input-dir 'inputs' \
    --output-dir "outputs_${ds}"
