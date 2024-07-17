class Data:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def interpolate(f: list, xi: int, n: int) -> float:
    result = 0.0
    for i in range(n):
        term = f[i].y
        for j in range(n):
            if j != i:
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)
        result += term
    return result
if __name__ == "__main__":
    f = [Data(20,18),Data(21,17),Data(24,15),Data(26,14),Data(27,16),Data(28,15)]
    print("Value of f(23) is : ", interpolate(f,23,6))