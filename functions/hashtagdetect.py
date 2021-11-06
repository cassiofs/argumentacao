import re
text = "#hashtag01 # aqui nada #hashtag2 #123"
hashtags = re.findall(r'\B#\w*[a-zA-Z]+\w*', text)
if hashtags:
	print(hashtags)
else:
	print("Nada")
