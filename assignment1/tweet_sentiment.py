import sys
import json
from StringIO import StringIO

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = {} # initialize an empty dictionary
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	for line in tweet_file:
		io = StringIO(line)
		obj = json.load(io)
		sent = 0
		if obj.has_key('text'):
			wordCount = 0
			for word in obj['text'].split(" "):
				wordCount = wordCount + 1
				if scores.has_key(word):
					sent = sent+ scores[word]
				else:
					pass
					#print "word ",word," not in score"
			sent = sent / wordCount
		print sent
		
if __name__ == '__main__':
    main()
