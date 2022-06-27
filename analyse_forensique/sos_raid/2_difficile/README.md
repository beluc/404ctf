SOS RAID [2/2]
982

Bravo, vous avez réussi à récupérer les données. Cependant, il s'avère que l'un des fichiers a été corrompu pendant la copie. Pouvez-vous le réparer pour en extraire des informations ?

Auteur : Typhlos#9037

Changer la signature du png + taille IHDR (13) :
89 50 4E 47  0D 00 00 0A  00 00 FF 0D => 89 50 4E 47  0D 0A 1A 0A  00 00 00 0D

pngcheck -vf flag_c0rr_pt3d.png
File: flag_c0rr_pt3d.png (61863 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1152 x 62088 image, 32-bit RGB+alpha, non-interlaced
  CRC error in chunk IHDR (computed 6c55bbd4, expected 082b810d)
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 3780x3780 pixels/meter (96 dpi)
  chunk IDAT at offset 0x00057, length 61756
    zlib: deflated, 32K window, fast compression
  chunk IEND at offset 0x0f19f, length 173:  EOF while reading data
ERRORS DETECTED in ../1_facile/flag_c0rr_pt3d.png

changer le crc IHDR :
08 2B 81 0D => 6C 55 BB D4

pngcheck -vf flag_c0rr_pt3d.png
File: flag_c0rr_pt3d.png (61863 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1152 x 62088 image, 32-bit RGB+alpha, non-interlaced
  CRC error in chunk IHDR (computed 6c55bbd4, expected 082b810d)
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 3780x3780 pixels/meter (96 dpi)
  chunk IDAT at offset 0x00057, length 61756
    zlib: deflated, 32K window, fast compression
  chunk IEND at offset 0x0f19f, length 173:  EOF while reading data
ERRORS DETECTED in flag_c0rr_pt3d.png

changer la taille IEND (toujours 0):
00 00 00 AD  49 45 4E 44  AE 42 60 82 => 00 00 00 00  49 45 4E 44  AE 42 60 82

pngcheck -vf flag_c0rr_pt3d.png
File: flag_c0rr_pt3d.png (61863 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1152 x 62088 image, 32-bit RGB+alpha, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 3780x3780 pixels/meter (96 dpi)
  chunk IDAT at offset 0x00057, length 61756
    zlib: deflated, 32K window, fast compression
  chunk IEND at offset 0x0f19f, length 0
No errors detected in flag_c0rr_pt3d.png (6 chunks, 100.0% compression).

=> 404CTF{L4_C0rr_pt1ON_s3_r_p4r_}
