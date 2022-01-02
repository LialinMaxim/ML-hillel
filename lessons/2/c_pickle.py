import pickle
import os
PATH = 'myconfig.bin'

if os.path.exists(PATH):
    with open(PATH, 'rb') as f:
        d = pickle.load(f)
        pass
else:
    d = {'key': 'value'}
#
# with open(PATH, 'wb') as f:
#     pickle.dump(d, f)


