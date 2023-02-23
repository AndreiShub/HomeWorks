import re

string = r"Red	(255, 0,0)	#FF0000 Green	(0,255,0)	#00FF00Blue(0, 0,255)	#0000FF"
result_hex = re.findall(r"\#[A-F0-9]{6}",string)
result_rgb = re.findall(r"\(\d+,[ ]{0,1}\d+,[ ]{0,1}\d+\)",string)
print(result_hex, result_rgb)