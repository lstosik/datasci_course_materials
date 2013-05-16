SELECT count(*) FROM (
	select f1.docid 
	from frequency f1, frequency f2 
	where f1.docid=f2.docid 
		and f1.term = 'transactions' 
		and f2.term = 'world'
);
