# Causa e efeito, Explicação, Restrição, Finalidade (ex: a fim de, como consequência, dado que, devido a, isto é, já que, logo, ou seja, para, pois, por, por conta de, por isso, porque, portanto, posto que, visto que)
import re
text = "veremos que, assim como, dado que, o outro também"
hashtags = re.findall(r'a fim de|como consequência|dado que|devido a|isto é|já que|logo|ou seja|para|pois|por|por conta|por isso|porque|portanto|posto que|visto que', text)
if hashtags:
	print(hashtags)
else:
	print("Nada")


