class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]
        i=1
        while i <=n:
            if i%5==0 and i%3==0:
                res.append('FizzBuzz')
            elif i%5==0:
                res.append('Buzz')
            elif i%3==0:
                res.append('Fizz')
            else:
                res.append(str(i))
            
            i+=1
        return res
