def find_volume(height=1, width=1, depth=1):
    return height * width * depth, height, 'Hola'

volume,height,string = find_volume(10,20,30)
print(volume)
print(height)
print(string)
volume = find_volume()
print(volume)
volume = find_volume(20)
print(volume)