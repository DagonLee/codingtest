def lotto_gen(num_list: list, store: list, idx: int):
	if len(store) == 6:
		for i in range(6):
			print(store[i], end=' ')
		print()
		return
	if idx == len(num_list):
		return
	store.append(num_list[idx])
	lotto_gen(num_list, store, idx + 1)
	store.pop()
	lotto_gen(num_list, store, idx + 1)

while True:
	_input = list(map(int, input().split()))
	if _input[0] == 0:
		break
	lst = _input[1:]
	lotto_gen(lst, [], 0)
	print()
