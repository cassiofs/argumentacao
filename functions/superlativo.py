# Superlativo
import re
text = "agradabilíssimo ou agradabilíssima. algumas outras palavras palpérrimo agradabilissima novamente laranja ilima isso é facílimo!!!"
superlativo = re.findall(r'\w*[í|i]ssim[a|o]|\w*[é|e]rrim[o|a]|\w*[í|i]lim[o|a]', text)
if superlativo:
	print(superlativo)
else:
	print("Nada")
