# EOF 처리문제

while True:
	try:
		A, B = map(int, input().split())
		print(A+B)
	except EOFError:
		break