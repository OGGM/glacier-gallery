**How to add a new glacier to the gallery**

1. Resize you photo that the longer side (height or width) equals 400px (linux: `convert -geometry 400x src/image1.png out/image1.png` for 400px width, or `convert -geometry x400 src/image1.png out/image1.png` for 400px height, aspect ratio is conserved)
2. Add the resized photo to `glacier_photos/`
3. Add new entry in `glacier_data.py` (for `img` use `https://raw.githubusercontent.com/OGGM/glacier-gallery/master/glacier_photos/NEW_GLACIER.jpg`) and save file
4. execute the whole notebook for each language (currently `en` and `de`) and save clean version of notebook afterwards
5. commit, push, merge

