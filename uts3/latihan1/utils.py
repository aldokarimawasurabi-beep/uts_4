def menghitung_nilai_terbesar(data):
	return max(data)
	
def menghitung_nilai_terkecil(data):
	return min(data)
	
def parse_list(list_string):
	return list(map(int, list_string.split()))