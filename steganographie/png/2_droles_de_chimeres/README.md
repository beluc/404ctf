PNG : Drôles de chimères [2/4]
932

Il semblerait que votre dernière analyse ait été fructueuse, mais nos analystes trouvent encore à redire. Il faudrait aller plus loin dans vos recherches et comprendre pourquoi la structure du fichier que vous nous avez remis leur paraît étrange, même si elle est parfaitement valide.

Auteur: Smyler#7078

Pour rappel, voici le fichier en question:

pngsplit stage2.png
cp -a stage2.png.0002.sTeG stage3.png
Remplacer 00 05 EC FE  73 54 65 47 par 89 50 4E 47  0D 0A 1A 0A dans stage3.png

pngcheck -vf stage3.png
File: stage3.png (388362 bytes)
  chunk IHDR at offset 0x0000c, length 13
    500 x 473 image, 32-bit RGB+alpha, non-interlaced
  chunk IDAT at offset 0x00025, length 8192
    zlib: deflated, 32K window, default compression
  chunk IDAT at offset 0x02031, length 8192
  chunk IDAT at offset 0x0403d, length 8192
  chunk IDAT at offset 0x06049, length 8192
  chunk IDAT at offset 0x08055, length 8192
  chunk IDAT at offset 0x0a061, length 8192
  chunk IDAT at offset 0x0c06d, length 8192
  chunk IDAT at offset 0x0e079, length 8192
  chunk IDAT at offset 0x10085, length 8192
  chunk IDAT at offset 0x12091, length 2213
  chunk IDAT at offset 0x12942, length 312240
  chunk IEND at offset 0x5ecfe, length 0
  additional data after IEND chunk
:  invalid chunk length (too large)
ERRORS DETECTED in stage3.png

truncate -s -4 stage3.png

pngcheck -vf stage3.png
File: stage3.png (388358 bytes)
  chunk IHDR at offset 0x0000c, length 13
    500 x 473 image, 32-bit RGB+alpha, non-interlaced
  chunk IDAT at offset 0x00025, length 8192
    zlib: deflated, 32K window, default compression
  chunk IDAT at offset 0x02031, length 8192
  chunk IDAT at offset 0x0403d, length 8192
  chunk IDAT at offset 0x06049, length 8192
  chunk IDAT at offset 0x08055, length 8192
  chunk IDAT at offset 0x0a061, length 8192
  chunk IDAT at offset 0x0c06d, length 8192
  chunk IDAT at offset 0x0e079, length 8192
  chunk IDAT at offset 0x10085, length 8192
  chunk IDAT at offset 0x12091, length 2213
  chunk IDAT at offset 0x12942, length 312240
  chunk IEND at offset 0x5ecfe, length 0
No errors detected in stage3.png (13 chunks, 58.9% compression).
