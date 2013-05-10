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
		if obj.has_key('entities'):
			e = obj['entities']
			if e.has_key('hashtags'):
				ht = e['hashtags']
				for tag in ht:
					text = tag['text']
					if scores.has_key(text):
						scores[text] = scores[text] + 1
					else:
						scores[text] = 1	
	#print sorted(scores)
	for word in sorted(scores.keys(), cmp=(lambda x,y :  cmp(scores[y],scores[x])))[0:10]:
		print word, 1.0*scores[word]
if __name__ == '__main__':
    main()

