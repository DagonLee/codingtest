def tag_func(tag, text):
	text = text
	tag = tag
	def inner_func():
		return '<{0}>{1}<{0}>'.format(tag, text)
	return inner_func


h1_func = tag_func('title', "This is Python Class")
p_func = tag_func('p', "Data Academy")

print(h1_func('h1안의태그입니다.'))