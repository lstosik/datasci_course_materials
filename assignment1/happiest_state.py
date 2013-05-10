import sys
import json
from StringIO import StringIO
import re
def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = {}
	states = {}
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	for line in tweet_file:
		io = StringIO(line)
		obj = json.load(io)
		if obj.has_key('place'):
			place = obj['place']
			if place == None:
				continue
			if not(place.has_key('country_code')) or place['country_code']!='US':
				continue
			score = 0
			if obj.has_key('text'):
				ex = re.split(r"\s", obj['text'], 0, re.UNICODE);
				for word in ex:
					if scores.has_key(word):
						score = score + scores[word]
			if place.has_key('full_name'):
				state = place['full_name'][-2:]
				if states.has_key(state):
					st = states[state]
					st['total'] = st['total'] + 1
					st['hap'] = st['hap'] + score
				else:
					st = {}
					st['total'] = 1
					st['hap'] =  score
					states[state] = st
#				print state, score
	list = []
	for state in states.keys():
		meta = states[state]
		meta['name'] = state
		meta['val'] = 1.0*meta['hap']/meta['total'] 
		list = list +[meta]
#		print state, 1.0*meta['hap']/meta['total']
	for state in sorted(list, cmp=(lambda x,y :  cmp(y['val'],x['val']))):
		print state['name']
		break
		
if __name__ == '__main__':
    main()

