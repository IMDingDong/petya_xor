import sys

def main():
	if len(sys.argv) < 1:
		sys.exit(1)

	result_list = []
	file = sys.argv[1]
	f = open(file, 'r')
	w = open("result.txt", 'w')
	hex_data = f.read()
	end_len = len(hex_data)

	for i in range(0, end_len, 2):
		data = str(hex(int(hex_data[i:i+2], 16) ^ int("37", 16))[2:])
		if len(data) == 1:
			data = '0' + data
		w.write(data)

	w.close()
	f.close()

if __name__ == '__main__':
	main()