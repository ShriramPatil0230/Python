class Vec2d:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class Vec3d(Vec2d):
    def __init__(self, i, j, k):
        super().__init__(i ,j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d= Vec2d(1,2)
v3d= Vec3d(2,4,6)
print(v2d)
print(v3d)