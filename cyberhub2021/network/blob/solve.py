import base64
from itertools import permutations

def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str
seq = permutations(["INLZL52DAX","MN4WEZLSNB","3DGR2GG2D5","2WE63QMF","RWWM3UONP","W4MDUL5ST"])
for p in list(seq):
   c = convertTuple(p)
   de = base64.b32decode(c)
   if 'cyberhub{' in str(de) and r'\x' not in str(de):
   	print('flag is: '+de.decode('utf-8'))
