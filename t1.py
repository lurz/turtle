from PIL import Image
from PIL import PSDraw

mimage = Image.open("molecule.png")
limage = Image.open("logo.png")

# resize logo
# wsize = int(min(mimage.size[0], mimage.size[1]) * 0.25)
# wpercent = (wsize / float(limage.size[0]))
# hsize = int((float(limage.size[1]) * float(wpercent)))

# simage = limage.resize((wsize, hsize))
simage = limage
mbox = mimage.getbbox()
sbox = simage.getbbox()
print(mbox)
print(sbox)
# right bottom corner
box = (mbox[2] - sbox[2], mbox[3] - sbox[3])
print(box)
box = (0,0)
mimage.paste(simage, box)
mimage.save("out.png")

            http://192.168.86.51:8080/stream?topic=/usb_cam/image_raw
