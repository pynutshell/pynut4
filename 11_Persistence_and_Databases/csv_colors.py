import csv

color_data = """\
color,r,g,b
red,255,0,0
green,0,255,0
blue,0,0,255
cyan,0,255,255
magenta,255,0,255
yellow,255,255,0
""".splitlines()

colors = {row["color"]: row
          for row in csv.DictReader(color_data)}

print(colors["red"])  # prints {'color': 'red', 'r': '255', 'g': '0', 'b': '0'}
