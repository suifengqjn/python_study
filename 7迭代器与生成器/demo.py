
#使用生成器输出素数
class PrimeNumbers:
    def __init__(self,start, end):
        self.start = start
        self.end = end
    def isPrime(self, k):
        if k <=2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True
    def __iter__(self):
        for k in range(self.start, self.end+1):
            if self.isPrime(k):
                yield k




#测试
for i in PrimeNumbers(1, 100):
    print("素数",i)


