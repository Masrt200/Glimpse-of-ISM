from PIL import Image
import os
import random

images=os.listdir()
images.remove('strip_gen.py')
images.remove('make')
print(images)

Y=450
X=600

imf=Image.new('RGB', (X,Y*4))
pixy=imf.load()

ims=[]
for k in range(len(images)):

	im=Image.open(images[k])
	print(im.mode,im.size)
	
	im1=im.resize((X,Y))
	print(im1.size)
	ims.append(im1)
	

pix_wid=3
files=4

for j in range(0,1800,files*pix_wid):
	for k in range(4):
		pixels=ims[k].load()
		for l in range(pix_wid):
			for i in range(X):
				pixy[i,j+pix_wid*k+l]=pixels[i,j//4+l]


imf.save("make/chaii.png")

