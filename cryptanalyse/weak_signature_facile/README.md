Weak Signature
995

Un nouveau système a été mis en place pour exécuter du code de façon sécurisée sur l'infrastructure. Il suffit d'envoyer une archive signée et encodée en base 64 pour exécuter le code Python qu'elle contient !

Vous trouverez la documentation de ce système et un exemple en pièces jointes. Tentez de voir si vous ne pourriez pas l'exploiter afin de lire le précieux fichier flag.txt

Auteur : Cyxo#0458
nc challenge.404ctf.fr 32441 

On remarque que le checksum est assez faible. on réécrit le .zsig pour que la donnée ait la même taille et le même checksum tout en ajoutant le code pour lire le drapeau
