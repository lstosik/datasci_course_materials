import MapReduce
import sys

"""
Inverted Index
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	rtype = record[0]
	rid = record[1]
	mr.emit_intermediate(rid, record)
	

def reducer(key, list_of_values):
	order = list_of_values[0]
	for line in list_of_values[1:]:
		mr.emit(order + line)
#   

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
