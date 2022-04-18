# Introduction
----
> As, this is a QR code, So here some colors represents **Black** and others represents **White**
# Hacking Steps
----
- Identify total number of colors in the picture
- Make a list that contains all the possible combinations of the indetified colors
- Try and Test all the possible combinations to get the right one

```python
#!/usr/bin/env python3

from PIL import Image
from pyzbar.pyzbar import decode 
from itertools import combinations


qr = Image.open("./hackit.png")
data = qr.load()
size = qr.size

temp = Image.new(qr.mode,qr.size)
mal = temp.load()


konwColor = set()
black = (255,255,255)
white = (0,0,0)


for i in range(size[0]): #width
	for j in range(size[1]): #height
		color = data[i,j]
		if(color != black and color != white):
			konwColor.add(color)
# print(konwColor)
# exit()

for i in range(len(konwColor)):
	trails = combinations(konwColor,i+1)

	for cList in trails:
		# print(cList)
		# continue
		for j in range(size[0]): #width
			for k in range(size[1]): #height
				color = data[j,k]

				if color == black or color == white:
					mal[j,k] = color
				elif color in cList:
					mal[j,k] = black
				else:
					mal[j,k] = white

		msg = decode(temp)
		if(msg):
			print(msg[0].data.decode())
```


