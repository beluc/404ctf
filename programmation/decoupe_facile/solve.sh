for i in `seq 1 576`; do source="$source output/$i.png"; done
montage -geometry 20x20 -tile 24x24 $source final.png

