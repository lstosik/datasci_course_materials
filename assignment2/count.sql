SELECT count(*) FROM (
	select docid from frequency WHERE term = 'parliament'
);
