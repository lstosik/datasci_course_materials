import sys
import json
from StringIO import StringIO
import re
def main():
	tweet_file = open(sys.argv[1])
	scores = {}
	total = 0

	for line in tweet_file:
		io = StringIO(line)
		obj = json.load(io)
		if obj.has_key('text'):
			list = []
			ex = re.split(r"\s", obj['text'], 0, re.UNICODE);
			for word in ex:
				if len(word)<1:
					continue
				total = total + 1
				if scores.has_key(word):
					scores[word] = scores[word] + 1
				else:
					scores[word] = 1
	for word in scores.keys():
		if len(word)<1:
			continue
		out = ""+word+ " "+ str(1.0*scores[word]/total)
		if len(out)<3:
			continue
		print out.encode('utf-8')
		
if __name__ == '__main__':
    main()

