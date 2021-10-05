import re
lig_dict = {'AE': '[AE]', 'Ae': '[AE]', 'aE': '[ae]', 'ae': '[ae]', 'OE': '[OE]','Oe': '[OE]', 'oE': '[oe]', 'oe': '[oe]',
			'ct': '[ct]', 'ffi': '[ffi]', 'ffl': '[ffl]', 'ff': '[ff]', 'fi': '[fi]', 'fl': '[fl]',
			'sss': 'ㄱ', 'ss': 'ㄴ', 'si': 'ㄷ', 'sh': 'ㄹ', 'sl': 'ㅁ',
			'st': 'ㅂ', 'ssi': 'ㅅ', 's': 'ㅇ'}
s_dict = {'ㅍ': 's', 'ㄱ': 's[longs]s', 'ㄴ': '[longsi]', 'ㄷ': '[longsh]', 'ㄹ': '[longsl]', 'ㅁ': '[longss]', \
			'ㅇ':'[longs]', 'ㅂ': '[longst]', 'ㅅ': '[longssi]'}

for _ in range(int(input())):
	s = input()
	## short s 처리
	while re.search('(s[^a-zA-Z])|(sf)|(sb)|(sk)', s):
		matchobj = re.search('(s[^a-zA-Z])|(sf)|(sb)|(sk)', s)
		print(matchobj)
		re.sub(matchobj.group(), 'ㅍ', s)

	# pattern2 = re.compile('s$')
	# a = pattern.()
	# for key in lig_dict:
	# 	s = re.sub(key, lig_dict[key], s)
	#
	# for key in s_dict:
	# 	s = re.sub(key, s_dict[key], s)
	# print(s)