import os
import re

comment = os.getenv('PR_COMMENT', '')
match = re.search('/wandb[\s+](\S+)', comment)

with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    if match:
        print('VAL_FOUND=true', file=f)
        print(f'RUN_ID={match.group(1)}', file=f)
    else:
        print('VAL_FOUND=false', file=f)