import os
files = os.listdir('.')
files = [f for f in files if f.endswith('.rar')]

for f in files:
    os.system('git add "' + f + '"')
    os.system('git commit -m "Add ' + f + '"')
    os.system('git push')
    os.system('git fetch')