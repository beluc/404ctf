 128code128
977

Nous avons envoyé un agent infiltrer un entrepôt suspect. Hélas le voilà désormais bloqué dans un dédale de portes ! Il semblerait que ces portes ne s'ouvrent qu'avec un code étrange que seuls les robots tueurs patrouillant dans le secteur semblent capables de déchiffrer... Heureusement, cet agent est en contact avec vous ! Aidez-le à décoder ces images et à ouvrir les portes pour qu'il puisse s'échapper ! Attention, si vous êtes trop lent ou que vous faites la moindre erreur, l'alarme retentira... Bonne chance !

Auteur: mh4ckt3mh4ckt1c4s#0705
nc challenge.404ctf.fr 30566 


====
Ma solution pour code128code:
À lancer dans deux shells :
tee $(tty) < fifo | while read l2; do echo $l2 | base64 -d | convert - txt: | grep ,1: | sed -e "s/.*e$/0/g" -e "s/.*k$/1/g" | awk '{ print; } NR % 11 == 0 { print " "; }' | tr -d "\n" | sed "s/ /\n/g" | while read l; do grep $l code128.txt; done | cut -d$'\t' -f 4 | tr -d "\n" | sed -e '$a\' ; done > fifo2
et nc challenge.404ctf.fr 30566 < fifo2 > fifo (où code128.txt est un copier-coller du tableau de wikipedia sur le code128)

cpiod
 — 
Aujourd’hui à 17:03
Il faut créer des fifo avec mkfifo (mkfifo fifo et mkfifo fifo2), installer quelques paquets (imagemagick, awk, nc notamment). Le fichier code128.txt est joint. Enfin, j’ai utilisé zsh, donc pas sûr que ça marche sur bash. Bref, mon message était plus pour flexer que pour vraiment être utilisé…


