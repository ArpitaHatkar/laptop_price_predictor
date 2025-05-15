#Model use

from pickle import load

with open("laptop_model.pkl","rb")as f:
	model = load(f)

r = int(input("RAM --> 1 for 8GB, 2 for 12GB and 3 for 16GB"))

if r == 1:
	d1 = [8]
elif r == 2:
	d1 = [12]
else:
	d1 = [16]

d = int(input("DISPLAY --> 1 for 14 and  2 for 15.6"))
if d == 1:
	d2 = [14]
else:
	d2 = [15.6]

p = int(input("PROCESSOR --> 1 for i3, 2 for i5, 3 for i7 and 4 for i9"))
if p == 1:
	d3 = [1,0,0,0]
elif p == 2:
	d3 = [0,1,0,0]
elif p == 3:
	d3 = [0,0,1,0]
else:
	d3 = [0,0,0,1]

s = int(input(" SSD --> 1 for 1 TB and 2 for 512 GB"))
if s == 1:
	d4 = [1,0]
else:
	d4 = [0,1]

b = int(input("BRAND --> 1 for acer, 2 for asus, 3 for dell, 4 for hp and 5 for lenovo"))
if b == 1:
	d5 = [1,0,0,0,0]
elif b == 2:
	d5 = [0,1,0,0,0]
elif b == 3:
	d5 = [0,0,1,0,0]
elif b == 4:
	d5 = [0,0,0,1,0]
else:
	d5 = [0,0,0,0,1]

g = int(input("GPU --> 1 for na, 2 for rtx3040 and 3 for rtx3060"))
if g == 1:
	d6 = [1,0,0]
elif g == 2:
	d6 = [0,1,0]
else:
	d6 = [0,0,1]
d = [d1 + d2 + d3 + d4 + d5 + d6]
price = model.predict(d)
print(price)