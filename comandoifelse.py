
from ast import pattern
import re 

pattern = re.compile(r"(if)([\s])*(\[)([\s])*([\w])+([\s])*((-eq)|(-ne)|(-gt)|(-lt)|(-ge)|(-le))([\s])*([\w])+([\s])*(\])(\;)([\s])*(\w)+(\;)([\s])*(elif)([\s])*(\[)([\w])+([\s]*)((-eq)|(-ne)|(-gt)|(-lt)|(-ge)|(-le))([\s]*)([\w])+(\])([\s]*)(\;)([\s]*)(\w)+([\s]*)(\;)([\s]*)(else)([\s]*)(\w)+(\;)([\s]*)(fi)", flags=re.M)

with open('comandoif.txt', 'r') as arquivo:
  var = arquivo.read()
  
result = re.findall(pattern, var)
print(result)


