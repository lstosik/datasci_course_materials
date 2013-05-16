select sum(part) from (
	select f1.count*f2.count as part
	from frequency f1, frequency f2 
	where f1.docid = '10080_txt_crude'
		and f2.docid = '17035_txt_earn'
		and f1.term = f2.term
)
;
