# Superlativo / exagero
import re
text = "agradabilíssimo ou agradabilíssima. algumas outras palavras palpérrimo agradabilissima novamente laranja ilima isso é facílimo!!! túnica infinitamente unicamente"
superlexagero = re.findall(r'\w*[í|i]ssim[a|o]|\w*[é|e]rrim[o|a]|\w*[í|i]lim[o|a]|[ú|u]nic[o|a]|nunca|sempre|exatamente|infinitamente', text)

 #“única/o”, “todo/a”, “nunca”, “sempre”, “exatamente”, “infinitamente”

if superlexagero:
	print(superlexagero)
else:
	print("Nada")
