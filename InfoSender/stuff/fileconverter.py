import sys
import base64

if len(sys.argv) == 1:
    print("No file!")
    quit()

filename = sys.argv[1]

file = open(filename, "r")
content_raw = file.read()

temp = content_raw.split("\n")

content = "".join(temp)

buffer = base64.decodebytes(bytes(content, "utf8"))
file.close()

final = open("lil pump ayy esketit.txt", "wb")
final.write(buffer)
final.close()