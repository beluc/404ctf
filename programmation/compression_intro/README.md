 Compression
100

Après une intervention, nous avons récupéré un fichier ultra-secret : le Fichier Légitime Arbitrairement Gros. Abrégé en "flag", nous pensons qu'il contient des secrets de Hallebarde. Hélas, comme ce fichier est supposément très lourd, il a été compressé un très grand nombre de fois de plusieurs manières différentes et nous n'arrivons pas à en récupérer le contenu. Pouvez-vous nous y aider ?

Auteur : mh4ckt3mh4ckt1c4s#0705

$ for i in `seq 2500 -1 1`; do echo flag$i.* && tar xf flag$i.*; done
$ cat flag.txt
404CTF{C0mPr3Ssi0n_m4X1m4L3_m41S_p4S_3ff1C4c3}
