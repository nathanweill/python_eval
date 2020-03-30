import os

from ruler import Ruler

script_dir = os.path.dirname(__file__)

file = open(os.path.join(script_dir, 'Dataset'))
while True:
    try:
        l1 = next(file).replace('\n', '')
        l2 = next(file).replace('\n', '')
        ruler = Ruler(l1, l2)
        ruler.compute()
        print(ruler.distance)
        top, bottom = ruler.report()
        print(top)
        print(bottom)
    except StopIteration:
        break


