class StringCalculator:
    
    def add(self,numbers:str)->int :
        
        if not numbers:
            return 0
        
        delimiter = ","
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[3:]
        
        numbers = numbers.replace("\n", delimiter)
        num = 0
        for i in numbers.split(delimiter):
            if i:
                num += int(i)
                if int(i) < 0:
                    raise ValueError("negatives not allowed")
        
        return num