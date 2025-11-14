def sort_dictionary(d):
	asc_key=dict(sorted(d.items()))
	print("Ascending order by keys:",asc_key)
	dec_key=dict(sorted(d.items(),key=lambda x:-x[0]))
	print("Descending order by keys:",dec_key)
	asc_value=dict(sorted(d.items(),key=lambda x: x[1]))
	print("Ascending order by values:",asc_value)
	dec_value=dict(sorted(d.items(),key=lambda x:-x[1]))
	print("Descending order by values:",dec_value)
d={3:5, 1:6, 8:30, 2:11}
sort_dictionary(d)
