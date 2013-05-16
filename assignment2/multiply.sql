select sum(part) from (
	select a.value*b.value as part from a,b where a.row_num = 2 and a.col_num = b.row_num and b.col_num = 3
);
