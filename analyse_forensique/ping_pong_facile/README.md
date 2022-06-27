Ping Pong
837

Nous avons repéré une communication bizarre provenant des serveurs de Hallebarde. On soupçonne qu'ils en aient profité pour s'échanger des informations vitales. Pouvez-vous investiguer ?

Auteur : Typhlos#9037

tshark -r ping.pcapng -T fields -e data.len icmp.type == 8 | awk '{printf "%c", $1}'

404CTF{Un_p1ng_p0ng_p4s_si_1nn0c3nt}
