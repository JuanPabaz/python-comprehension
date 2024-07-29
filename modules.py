import sys
import re
import time

print(sys.path)
text = 'Mi numero de telefono es 300 8298941, el codigo del pais es +57, mi numero de la suerte es el 3.'
print(re.findall('[0-9]+',text))
time_now = time.time()
local_date = time.localtime()
result = time.asctime()
print(result)