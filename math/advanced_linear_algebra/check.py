import importlib
import numpy as np

det = importlib.import_module('0-determinant').determinant
minor = importlib.import_module('1-minor').minor
cof = importlib.import_module('2-cofactor').cofactor
adj = importlib.import_module('3-adjugate').adjugate
inv = importlib.import_module('4-inverse').inverse
defin = importlib.import_module('5-definiteness').definiteness

mats = [[[5]], [[1, 2], [3, 4]], [[1, 1], [1, 1]],
        [[5, 7, 9], [3, 1, 8], [6, 2, 4]], [], [[1, 2, 3], [4, 5, 6]]]

for name, f in [('det', det), ('minor', minor), ('cofactor', cof),
                ('adjugate', adj), ('inverse', inv)]:
    print('---', name)
    for m in ([[]] + mats if name == 'det' else mats):
        try:
            print(f(m))
        except Exception as e:
            print(e)

print('--- definiteness')
for m in [np.array([[5, 1], [1, 1]]), np.array([[2, 4], [4, 8]]),
          np.array([[-1, 1], [1, -1]]), np.array([[-2, 4], [4, -9]]),
          np.array([[1, 2], [2, 1]]), np.array([]),
          np.array([[1, 2, 3], [4, 5, 6]]), [[1, 2], [1, 2]]]:
    try:
        print(defin(m))
    except Exception as e:
        print(e)
