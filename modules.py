import sys
import re
import time
import collections

print(sys.path)
text = 'Mi numero de telefono es 300 8298941, el codigo del pais es +57, mi numero de la suerte es el 3.'
print(re.findall('[0-9]+',text))
time_now = time.time()
local_date = time.localtime()
result = time.asctime()
print(result)

numbers = [1,2,3,4,21,2,21,2,1,3,4]
counter = collections.Counter(numbers)
print(counter)

