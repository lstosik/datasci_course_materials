#!/bin/sh
sqlite3 reuters.db < select.sql |tee select.txt
sqlite3 reuters.db < select_project.sql |tee select_project.txt 
sqlite3 reuters.db < union.sql |tee union.txt 
sqlite3 reuters.db < count.sql |tee count.txt 
sqlite3 reuters.db < big_documents.sql |tee big_documents.txt 
sqlite3 reuters.db < two_words.sql |tee two_words.txt 
sqlite3 matrix.db < multiply.sql |tee multiply.txt 
sqlite3 reuters.db < similarity_matrix.sql |tee similarity_matrix.txt
sqlite3 reuters.db < keyword_search.sql |tee keyword_search.txt
rm -f *.sql~

