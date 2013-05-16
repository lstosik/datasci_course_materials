SELECT count(*) FROM (
		select term from frequency WHERE docid = '10398_txt_earn' and count = 1
	union
		select term from frequency WHERE docid = '925_txt_trade' and count = 1
);
