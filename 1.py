import os
def b(fn,d):
	f=open(fn+".html"
f0=open("index.html","w")
f0.write("<html>\n<body>\n")
#../AndhrapAThaH/1_bAlakANDam/02-putrakAmaH/005_City_ayodhya_detailed.md
for d1 in sorted(os.listdir("AndhrapAThaH/")):
	if d1=="_index.md":continue
	f0.write("<a href=\"AndhrapAThaH/"+d1+".html>"+d1+"</a><br>\n")
	f1=open("AndhrapAThaH/"+d1+".html")
	f1.write("<html>\n<body>\n")
	f1.close()
f0.write("</body>\n</html>")
f0.close()
