string = "4/2@PAu<+ViNgg%^5NS`#J\u001fNK<XNW(_"
out = ""
for i in range(len(string)):
    out += chr(ord(string[i]) + i)

print(out)
