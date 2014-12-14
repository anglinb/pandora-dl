import sys, time, re, os, time, requests, pprint

# mat = re.compile("^www");
os.chdir('output');
mat = re.compile("^audio-.*pandora\.com|^.*p-cdn\.com");
anything = re.compile("\*.com")
logfile = open('songs.txt', 'w')
anything_logfile = open('logfile.txt','w')
while True:
	line = sys.stdin.readline()
	if line:
		if mat.match(line):
			parts = line.split('\t')
			for i, val in enumerate(parts):
				parts[i] = val.strip()

			pprint.pprint(parts)
			url = "http://"+parts[0]+parts[1]
			print url
			request = requests.get(url, stream=True)
			filepath = os.path.join(os.curdir, str(time.time())+'_audio.mp3')
			with open(filepath, "wb") as code:
				for chunk in request.iter_content(1024):
					if not chunk:
						break
					code.write(chunk)
			logfile.write(line)
			print 'Got data:', line
		elif anything.match(line):
			anything_logfile.write(line)