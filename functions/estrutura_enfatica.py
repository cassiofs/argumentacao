import re
frase = "@jandira_feghali OI FANTASMA, VC APARECE DE VEZ ENQDO PRA ATACAR O 'PRESIDENTE' DA MAIORIA DOS BR????? sabe o que vc tem que fazer, PROVAR QUE É MENTIRA  ... vcs acham mesmo que vai nos seduzir com NARRATIVAS ? E VC, JÁ PAGOU FUNCIONÁRIOS QUE ENTRARAM CONTRA VC NA JUSTIÇA ?"
estr_enf = 0

estr_enf_regex = re.findall(r"\B[\"|\']\w*[ a-zA-Z ]+\w*[\"|\']", frase)
if estr_enf_regex:
  estr_enf += 1

frase = frase.split()
for palavra in frase:
  if len(palavra) >3 and palavra.isupper():
    estr_enf += 1

if estr_enf:
  print(estr_enf)
else:
  print("Nada")
