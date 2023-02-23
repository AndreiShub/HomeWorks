import re

string = r"he ExpressiXIв IXвек XVI-XVIIввon & Text to see matches. Roll over matches or the \
expression for details. PCRE & JavaScript flavors of RegEx are supported. Validate your expr \
ession with Tests mode.merals such as IV, XIII, and MVIII."
result = re.findall(r"[XVI]+", string)
print(result)