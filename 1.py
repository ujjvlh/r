import os
def b(fn):
	f=open(fn+".html","w")
	f.write("<html>\n<body style=\"word-spacing:-.25em;\">\n")
	if os.path.isfile("../"+fn):
		fi=open("../"+fn,"r")
		html=fi.read()
		f.write("<audio controls playb id=\"ac\"><source src=\""+html[html.find('https'):html.find('mp3')+3]+"\" type=\"audio/mpeg\"></audio>")
		f.write(html[html.find('</div>')+6:].replace('\n','<br>\n').replace(' ',''))
		f.write("<script>ac.playbackRate=0.5</script>")
		fi.close()
	else:
		os.mkdir(fn)
		for d in sorted(os.listdir("../"+fn)):
			if d=="_index.md":continue
			f.write("<a href=\""+fn.split('/')[-1]+"/"+d+".html\">"+d+"</a><br>\n")
			b(fn+"/"+d)
		f.write("</body>\n</html>")
	f.close()
b("AndhrapAThaH")
#../AndhrapAThaH/1_bAlakANDam/02-putrakAmaH/005_City_ayodhya_detailed.md

