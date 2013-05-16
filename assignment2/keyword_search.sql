select sum(part),docid from (
	select f1.count*f2.count as part, f1.docid
	from frequency f1, (
		SELECT 'q' as docid, 'washington' as term, 1 as count 
		UNION
		SELECT 'q' as docid, 'taxes' as term, 1 as count
		UNION 
		SELECT 'q' as docid, 'treasury' as term, 1 as coun) as  f2 
	where 
		f1.term = f2.term
) group by docid order by 1 desc limit 1
;
