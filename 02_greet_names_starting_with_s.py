#write a program to greet names starting with letter 's'
from turtledemo.penrose import start

l = ["Harry", "Sujal", "Sersi", "Chris", "Isle", "Stark"]

for name in l:
    if name.startswith("S"):
        print(f"Good morning {name}")
    else:
        continue