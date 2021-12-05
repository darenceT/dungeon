
class obj:
    def __init__(self, impass=False):
        self.impass= impass

dict = {}


dict[1] = obj()
dict[2] = obj(impass=True)
dict[3] = obj(impass=True)
count = 0
for i in dict:
    if dict[i].impass:
        count += 1
print(count)
