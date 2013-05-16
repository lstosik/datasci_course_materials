SELECT count(*) FROM (
	select docid from frequency group by docid having sum(count) > 300
);
