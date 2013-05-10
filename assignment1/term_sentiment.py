import sys
import json
from StringIO import StringIO

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = {} # initialize an empty dictionary
	newScores = {}
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	for line in tweet_file:
		io = StringIO(line)
		obj = json.load(io)
		sent = 0
		if obj.has_key('text'):
			wordCount = 0
			list = []
			for word in obj['text'].split(" "):
				wordCount = wordCount + 1
				if scores.has_key(word):
					sent = sent+ scores[word]
				else:
					list = list + [word]
					#print "word ",word," not in score"
			sent = sent / wordCount
			for nword in list:
				newScores[nword] = sent		
	for nWord in newScores.keys():
		if len(nWord)<1 or newScores[nWord]==0:
			continue
		out = ""+nWord+ " "+ str(newScores[nWord])
		print out.encode('utf-8')
		
if __name__ == '__main__':
    main()

