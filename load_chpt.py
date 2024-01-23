
import gdown
from pathlib import Path

for dir_name in 'checkpoints', 'inputs', 'outputs_lip', 'outputs_pascal':
    Path(dir_name).mkdir(parents=True, exist_ok=True)

dataset = 'pascal'

if dataset == 'lip':
    url = 'https://drive.google.com/uc?id=1k4dllHpu0bdx38J7H28rVVLpU-kOHmnH'
elif dataset == 'atr':
    url = 'https://drive.google.com/uc?id=1ruJg4lqR_jgQPj-9K0PP-L2vJERYOxLP'
elif dataset == 'pascal':
    url = 'https://drive.google.com/uc?id=1E5YwNKW2VOEayK9mWCS3Kpsxf-3z04ZE'
else:
    raise 1

# output = f'checkpoints/{dataset}.pth'
# gdown.download(url, output, quiet=False)


