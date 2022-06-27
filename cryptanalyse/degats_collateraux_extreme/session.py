from random import randint, getrandbits
from os import urandom
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
from inputimeout import inputimeout
from secret import flag, iv


def genkey():
    p = 53808220482511265213769064270473607140673708142612411473572970746759643108190355266906127944002960589365893851155124003324679468547911448179668629612593856353195368340854531316750551906191779683595128150002705287909603065461915859522271428558050829231120341984979440810262652371555379999679800336829254788066121743343520081225212413910077036117214295040812212949836484672274893827154827884909453862273676051009423127636581477353134375802649563771968793384060980184782565511473670072776942774379533383869937426213572690336231208502907798843337483044572824792553060089911695774585252820023442163104616243276986679352923
    # Le nombre premier utilisé change par période. En ce moment, c'est celui-ci.
    g = randint(2, p)
    x = getrandbits(1024)
    y = pow(g, x, p)
    return ((g, p, y), x)


def EGEncrypt( m, pubkey ):
    g, p, y = pubkey
    k = randint(2, p - 2)
    c0 = pow(g, k, p)
    c1 = (bytes_to_long(pad(m, 16)) * pow(y, k, p))
    return (c0, c1)


def EGDecrypt( c0, c1, g, p, x ):
    m1 = (c1 * pow(c0, -x, p)) % p
    m = unpad(long_to_bytes(m1), 16)
    return m


def oracle( pubkey, privkey, cipher, ciphered_key ):
    g, p, y = pubkey
    if p.bit_length() != 2049:
        return "Erreur: le module ne fait pas 2049 bits"
    c0, c1 = ciphered_key
    try:
        key2 = EGDecrypt(c0, c1, g, p, privkey)
    except:
        return "Erreur dans le déchiffrement, le fichier est peut-être corrompu"
    if not (is_session_key_valid(key2)):
        return "Erreur dans le déchiffrement, le fichier est peut-être corrompu"
    # Il semble qu'arrivé ici le serveur qui gère l'oracle lance d'autres fonctions / processus, mais nous n'avons pas
    # pu déterminer quoi
    aes = AES.new(key2, AES.MODE_CBC, iv=iv)
    try:
        pt = unpad(aes.decrypt(cipher), 16)
    except:
        return "Erreur dans le déchiffrement, le fichier est peut-être corrompu"
    if pt != flag:
        return "Erreur dans le déchiffrement, le fichier est peut-être corrompu"
    return "Le fichier est intact!"


def encrypt_flag( f, x ):
    hash = SHA256.new(data=long_to_bytes(x)).digest()
    aes = AES.new(hash [:16], AES.MODE_CBC, iv=hash [16:32])
    enc = aes.encrypt(pad(f, 16))
    return enc.hex()


def decrypt_flag( enc, x ):
    assert x.bit_length() == 1024
    hash = SHA256.new(data=long_to_bytes(x)).digest()
    aes = AES.new(hash [:16], AES.MODE_CBC, iv=hash [16:32])
    plaintext = unpad(aes.decrypt(bytes.fromhex(enc)), 16)
    return plaintext


def is_session_key_valid( session_key ):
    if len(session_key) == 16 and sum(session_key) % 31 == 0:
        return True
    return False


def pubkey_parser( s ):
    l = s.split(',')
    g = int(l [0] [1:])
    p = int(l [1])
    y = int(l [2] [:-1])
    return g, p, y


def pkesk_parser( s ):
    l = s.split(',')
    c0 = int(l [0] [1:])
    c1 = int(l [1] [:-1])
    return c0, c1


def create_session( plaintext, pubkey ):
    while True:
        sess_key = urandom(16)
        if is_session_key_valid(sess_key):
            break
    aes = AES.new(sess_key, AES.MODE_CBC, iv=iv)
    cipher = aes.encrypt(pad(plaintext, 16))
    ciphered_key = EGEncrypt(sess_key, pubkey)
    return cipher, ciphered_key, sess_key


def main():
    pubkey, privkey = genkey()
    g, p, y = pubkey
    enc = encrypt_flag(flag, privkey)
    print("Bonjour Agent,\nNous avons pu mettre en place une attaque MITM sur une connexion sécurisée d'Hallebarde")
    print(
        "Celle-ci est composée d'un émetteur, qui envoie à un oracle via une session PGP un fichier dans le but de vérifier son intégrité")
    print("Voici le fichier chiffré en question:")
    print(enc)
    print("Nous avons pu récupérer la clé publique de l'émetteur, la voici:")
    print(f"(g = {g}\np = {p}\ny = {y})")
    cipher, ciphered_key, sess_key = create_session(flag, pubkey)
    print(
        "Notre backdoor nous donne un contrôle assez fort, puisque nous pouvons modifier la PKESK a volonté.")
    print("Nous avons même la possibilité de réécrire la clé publique avant qu'elle soit utilisée par l'oracle.")
    print("Malheureusement, nous n'avons pas de contrôle sur le ciphertext")
    print(
        "Aucun de nos spécialistes n'a pu faire quoi que ce soit pour récupérer ce fichier en clair, voyez si vous pouvez faire quelque chose!")
    while True:
        print(
            "Modifier la clé publique? (format (g, p, y)) Laisser vide pour garder l'originelle")
        inp = inputimeout(prompt='>', timeout=120)
        try:
            if inp == '':
                key2 = pubkey
            else:
                key2 = pubkey_parser(inp)
        except:
            print("Erreur dans la lecture de la clé (N'oubliez pas les parenthèses)")
            continue
        print("Modifier la PKESK? (format (c0, c1)) Laisser vide pour garder l'originelle")
        inp = inputimeout(prompt='>', timeout=120)
        try:
            if inp == '':
                ciphered_key2 = ciphered_key
            else:
                ciphered_key2 = pkesk_parser(inp)
        except:
            print("Erreur dans la lecture de la clé (N'oubliez pas les parenthèses)")
            continue
        print("Valider l'envoi à l'oracle? [Y/n] Nous vous renverrons la réponse dès que nous l'aurons reçue")
        inp = inputimeout(prompt='>', timeout=30)
        if inp == 'n' or inp == 'non' or inp == 'no' or inp == 'N':
            continue
        ans = oracle(key2, privkey, cipher, ciphered_key2)
        print("Réponse reçue:")
        print(ans)


if __name__ == '__main__':
    main()
