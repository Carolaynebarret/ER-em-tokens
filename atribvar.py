
from ast import pattern
import re 

pattern = re.compile(r"^([a-zA-Z_]+|[0-9_a-zA-Z_])\s*([=])\s*(([\"][a-zA-Z]*[\"])|([\-\+]?[0-9]+)|(([$][\?\#\$\@\!0-9])|([$][a-zA-Z_]+)?))", flags=re.M)

with open('atribvariáveis.txt', 'r') as arquivo:
  var = arquivo.read()
  
result = re.findall(pattern, var)
print(result)


