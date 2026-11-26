from sys import path
path.append('..\\module') 

import moduleFile

print(__name__)

# print("Counter: ", moduleFile.__counter)

print(moduleFile.suml([10, 20, 30, 40, 50]))
print(moduleFile.prodl([10, 20, 30, 40, 50]))