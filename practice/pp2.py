class Calculator:
    def add(self, *args):
        return sum(args)

    def mul(self,*args):
        res=1
        for i in args:
            res*=i
        return res 
        
    def sub(self,*args):
        res=args[0]
        for i in args[1:]:
            res-=i
        return res
    
    def div(self,*args):
        res=args[0]
        for i in args[1:]:
            if i==0:
                return "Error: Division by zero"
            res/=i
        return res
calc=Calculator()
print("Addition:",calc.add(10,20,30))
print("sub:",calc.sub(10,20,30))
print("mul:",calc.mul(10,20,30))
print("div:",calc.div(10,20,30))