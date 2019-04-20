class Set:
    def __init__(self, member=[]):
        self.member = member
        le = list()
        for x in member:
            if x not in le:
                le.append(x)
        self.member = le

    def append(self, a):
        le = self.member
        if a not in self.member:
            le.append(a)


    def delete(self, a):
        # for idx, x in enumerate(self.member):
        #     if x == a:
        #         del self.member[idx]
        le = self.member
        if a in self.member:
            le.remove(a)
        # return le

    def union(self, s2):  # 합집합
        le = self.member
        for x in s2.member:
            if x in le:
                continue
            else:
                le.append(x)

        return le

    def intersection(self, s2):  # 교집합
        res = list()
        for x in self.member:
            if x in s2.member:
                res.append(x)
        return res

    def difference(self, s2):  # 차집합
        le = list()
        for x in self.member:
            if x not in s2.member:
                le.append(x)
        return le

    def __add__(self, member):
        res = self.union(member)
        return res

    def __sub__(self, member):
        res = self.difference(member)
        return res

    def __truediv__(self, member):
        res = self.intersection(member)
        return res

def main():
    a = Set([1, 2, 3])
    b = Set([1, 2, 3])

    c = a.union(b)
    print(c)

    d = a.difference(b)
    print(d)

    e = a.intersection(b)
    print(e)
    print("=============")

    c = a + b
    print(c)

    d = a - b
    print(d)

    e = a / b
    print(e)


if __name__ == "__main__":
    main()