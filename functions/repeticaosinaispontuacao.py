import re
text = "Olá???"
repetesinais = re.findall(r"[!|?]{2,}", text)
if repetesinais:
	print(repetesinais)
else:
	print("Nada")
