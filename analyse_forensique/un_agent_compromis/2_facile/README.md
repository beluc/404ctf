Un agent compromis [2/3]
923

Maintenant, nous avons besoin de savoir quels fichiers il a exfiltré.

Format du flag : 404CTF{fichier1,fichier2,fichier3,...} Le nom des fichiers doit être mis par ordre alphabétique.

Auteur : Typhlos#9037

import codecs

with open("exfiltration.dat") as f:
    filename = ""
    content = ""
    while True:
        line = f.readline().strip().replace(".hallebarde.404ctf.fr", "")
        if line == "":
            break
        if line == "never-gonna-give-you-up":
            filename = f.readline().strip().replace(".hallebarde.404ctf.fr", "")
            print(str(codecs.decode(filename, "hex"), "utf-8"))

404CTF{exfiltration.py,flag.txt,hallebarde.png,super-secret.pdf}
