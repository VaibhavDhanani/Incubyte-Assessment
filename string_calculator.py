class StringCalculator:
    
    def add(self,numbers:str)->int :
        
        if not numbers:
            return 0
        
        numbers = numbers.replace("\n", ",")
        num = 0
        for i in numbers.split(","):
            num += int(i)
        
        return num