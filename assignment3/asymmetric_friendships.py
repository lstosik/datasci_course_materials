import MapReduce
import sys

"""
Inverted Index
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	target = record[0]
	friendof = record[1]
	mr.emit_intermediate(target, ('incoming', friendof))
	mr.emit_intermediate(friendof, ('outgoing', target))

def reducer(key, list_of_values):
	def getSet(values, label):
		return set(map(lambda x:x[1], filter(lambda x:x[0]==label, list_of_values)))
	incoming = getSet(list_of_values, 'incoming')
	outgoing = getSet(list_of_values, 'outgoing')
	for x in incoming.symmetric_difference(outgoing):
		mr.emit((key, x))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
