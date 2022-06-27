import codecs

with open("exfiltration.dat") as f:
    filename = ""
    while True:
        line = f.readline().strip().replace(".hallebarde.404ctf.fr", "")
        if line == "":
            break
        elif line == "never-gonna-give-you-up":
            filename = str(codecs.decode(f.readline().strip().replace(".hallebarde.404ctf.fr", ""), "hex"), "utf-8")
            print(filename)
#        elif line == "626567696E": #begin
#            print("\tbegin")
#        elif line == "656E64": # end
#            print("\tend")
#            with open(filename, "wb") as ff:
#                ff.write(codecs.decode(content, "hex"))
#            content = ""
#        else:
#            content += line
