##################
# Daren McCulley #
# 7/21/16        #
################## Purpose ##################
# Simple script to balance a personally
# managed target retirement account.
#############################################

import sys

target_pcts = {'US Stocks': 54.1,
               'Intl Stocks': 36.7,
               'US Bonds': 6.5,
               'Intl Bonds': 2.7}

total = input('Enter total value of portfolio including money to invest: ')
try:
    float(total)
except:
    sys.exit('"%s" is not a valid input.' % total)

current_amts = {}
for k in target_pcts:
    try:
        v = input('Enter current value of %s: ' % k)
        current_amts[k] = float(v)
    except:
        sys.exit('"%s" is not a valid input.' % v)

target_amts = {k: float(total) * target_pcts[k] / 100.0 for k in target_pcts}

diffs = {k: int(target_amts[k] - current_amts[k]) for k in target_amts}

for k in diffs:
    print('Invest ${0:,} in {1}.'.format(diffs[k], k))

# EOF
