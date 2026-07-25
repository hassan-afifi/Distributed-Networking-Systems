import struct
import sys

files = sys.argv[1:5]
formats = [
    "?c9s",
    "9sif", 
    "fc?",
    "9s?i"
]

results = []
for i, filename in enumerate(files):
    try:
        with open(filename, 'rb') as f:
            data = f.read()
            if i == 0:
                size = struct.calcsize("?c9s")
            elif i == 1:
                size = struct.calcsize("9sif")
            elif i == 2:
                size = struct.calcsize("fc?")
            else:
                size = struct.calcsize("9s?i")
            
            if len(data) >= size:
                unpacked = struct.unpack(formats[i], data[:size])
                results.append(unpacked)
            else:
                print(f"Error: File {filename} too small")
    except Exception as e:
        print(f"Error reading {filename}: {e}")

for result in results:
    print(result)


data1 = struct.pack("18si?", b'elso', 76, True)
data2 = struct.pack("f?c", 79.5, False, b'X')
data3 = struct.pack("i16sf", 67, b'masodik', 86.9)
data4 = struct.pack("ci19s", b'Z', 98, b'harmadik')
print(data1)
print(data2)
print(data3)
print(data4)