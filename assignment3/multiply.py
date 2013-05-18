import MapReduce
import sys

"""
Inverted Index
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	matrix = record[0]
	i = record[1]
	j = record[2]
	value = record[3]
	if matrix=='a':
		for x in range(5):
			mr.emit_intermediate(str(i)+' '+str(x), (matrix, j, value))
	if matrix=='b':
		for x in range(5):
			mr.emit_intermediate(str(x)+' '+str(j), (matrix, i, value))

def reducer(key, list_of_values):
#	print key, list_of_values
	phases = set(map(lambda x:x[1],list_of_values))
	sum = 0
	i, j = map(int, key.split())
	for phase in phases:
		a = filter(lambda x:x[1]==phase and x[0]=='a',list_of_values)
		b = filter(lambda x:x[1]==phase and x[0]=='b',list_of_values)
		if len(a) > 0 and len(b)>0:
			sum = sum + a[0][2]*b[0][2]
	mr.emit((i,j,sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
