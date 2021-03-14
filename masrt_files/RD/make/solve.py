from PIL import Image


im=Image.open("chaii.png")
print(im.size)
pixy=im.load()

Y=450
X=600

ims=[]
pixs=[]
for i in range(4):
	im1=Image.new('RGB', (X,Y))
	pix=im1.load()
	ims.append(im1)
	#pixs.append(pix)

files=4
pix_wid=5
for j in range(0,1800,files*pix_wid):
	for k in range(4):
		pixels=ims[k].load()
		for l in range(pix_wid):
			for i in range(X):
				pixels[i,j//4+l]=pixy[i,j+pix_wid*k+l]
	

for i in range(4):
	ims[i].save(f"test{i}.png")