import re
text = "veremos que, assim como, o outro também"
hashtags = re.findall(r'assim como|da mesma forma|mal dá|quem dirá|nem um|nem outro|quanto mais|quem dirá', text)
if hashtags:
	print(hashtags)
else:
	print("Nada")
