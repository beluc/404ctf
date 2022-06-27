Hackllebarde ransomware [2/4]
997

Pour la suite de cette investigation, on vous donne accès à un dump mémoire d'une de nos stations qui a été compromise. Vous devez trouver la source de l'infection ! Aussi, il semblerait que le hackeur ait consulté des ressources depuis cette machine. Savoir quelles sont les techniques sur lesquelles il s'est renseigné nous aiderait beaucoup, alors retrouvez cette information !

Vous devez retrouver :

    une adresse IP distante qui a été contactée pour transmettre des données
    un numéro de port de la machine compromise qui a servi à échanger des données
    le nom d'un fichier exécutable malveillant
    un lien web correspondant à la ressource consultée par l'attaquant

Le flag est sous ce format : 404CTF{ip:port:binaire:lien} Par exemple, 404CTF{127.0.0.1:80:bash:https://google.fr/une-ressource-sympa/interessant.html} est un format de flag valide.

Somme de contrôle md5 du fichier extrait dumpmem.raw : dc2c324bf5fc80b6bf17a9def1b386ee

Auteur : mh4ckt3mh4ckt1c4s#0705
