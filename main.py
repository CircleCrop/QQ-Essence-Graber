import sys, os, subprocess
order = 1
cmd = 'python essence.py '
while order <= 1001:
    print('####')
    cout = cmd + str(order)
    order = order + 1
    os.system(cout)
