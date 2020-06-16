import os
def b(fn):
	f=open(fn+".html","w")
	f.write("<html lang=\"sa\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><body style=\"word-spacing:-.25em;margin:0;padding:0;\">\n")
	if os.path.isfile("../"+fn):
		f.write("<div style=\"display:flex;flex-flow:column;height:100%;\">")
		fi=open("../"+fn,"r")
		html=fi.read()
		f.write("<div style=\"display:flex;background-color:grey;padding:0.5em;flex: 0 1 auto;\">")
		f.write("<div style=\"flex: 0 1 auto;margin-top: auto;margin-bottom:auto;padding-right:1em;display:block;\"><button onclick=\"ac.currentTime-=5;\">⏪</button></div>")
		f.write("<audio controls id=\"ac\"><source src=\""+html[html.find('https'):html.find('mp3')+3]+"\" type=\"audio/mpeg\"></audio>")
		f.write("</div>")
		f.write("<div style=\"padding:0.5em;flex: 1 1 auto;overflow-y:auto;\">")
		f.write(html[html.find('</div>')+6:].replace('\n','<br>\n').replace(' ',''))
		f.write("</div>")
		f.write("</div>")
		f.write("<script>ac.playbackRate=0.5</script>")
		fi.close()
	else:
		os.mkdir(fn)
		f.write("<div style=\"padding:0.5em;\">")
		for d in sorted(os.listdir("../"+fn)):
			if d=="_index.md":continue
			f.write("<a href=\""+fn.split('/')[-1]+"/"+d+".html\">"+d+"</a><br>\n")
			b(fn+"/"+d)
		f.write("</div>")
	f.write("</body>\n</html>")
	f.close()
b("AndhrapAThaH")
#../AndhrapAThaH/1_bAlakANDam/02-putrakAmaH/005_City_ayodhya_detailed.md

