class StringCalculator:
    
    def add(self,numbers:str)->int :
        
        if not numbers:
            return 0
        
        num = [int(ele) for ele in numbers.split(',')]
        
        if len(num) == 2:
            return num[0] + num[1]
        
        if len(num) == 3:
            return num[0] + num[1] + num[2]
        
        
        return num[0]