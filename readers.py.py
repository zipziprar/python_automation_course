import csv

class CsvReader(object):

	def __init__(self):
		''''''

	def get_read(self, filename):
		container = []
		with open (filename, 'r') as opened_file:
			reader = csv.reader(opened_file)
			for row in reader:
				container.append(row)
		return container

f = CsvReader()
f.get_read('spt_list.csv')
print(f)

class TXTReader(object):
	''''''


class File(object):

	reader = {
		'.csv' : CsvReader(),
	}

	def get_symbol_index(self, file, symbol):
		return file.index(symbol)

	def get_file_format(self, file):
		return reader.get(file[get_symbol_index(file,'.'):])



file = File()
file.get_symbol_index('spt_list.csv', '.')
file.get_file_format('spt_list.csv')
