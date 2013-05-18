#!/bin/bash

check() {
	tmp=`mktemp`
	tmp2=`mktemp`
	python $1 "data/$2" |sort > $tmp
	cat "solutions/$3" |sort > $tmp2
	diff $tmp $tmp2 -q
	if [ $? -eq 0 ];then
		echo "$1 is giving proper output"
	elif [ $? -eq 1 ];then
		echo "$1 is giving wrong output"
	else
		echo "There was something wrong when checking $1"
	fi
	rm $tmp $tmp2
}
check "inverted_index.py" "books.json" "inverted_index.json"
check "join.py" "records.json" "join.json"
check "friend_count.py" "friends.json" "friend_count.json"
check "asymmetric_friendships.py" "friends.json" "asymmetric_friendships.json"
check "unique_trims.py" "dna.json" "unique_trims.json"
check "multiply.py" "matrix.json" "multiply.json"


