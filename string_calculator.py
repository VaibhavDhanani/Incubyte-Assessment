class StringCalculator:

    def __init__(self) -> None:
        self.__add_called_count = 0

    def get_called_count(self) -> int:
        return self.__add_called_count

    def add(self, numbers: str) -> int:
        self.__add_called_count += 1

        if not numbers:
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            i = 2
            temp_delimiter = ""
            
            if numbers[i] == "[":
                i += 1
                while i < len(numbers) and numbers[i] != "]":
                    temp_delimiter += numbers[i]
                    i += 1
                delimiter = temp_delimiter
            else:
                while i < len(numbers) and numbers[i] != "\n":
                    temp_delimiter += numbers[i]
                    i += 1
                delimiter = temp_delimiter
                
            numbers = numbers[i+1:]
                
        numbers = numbers.replace("\n", delimiter)

        
        num = 0
        negative_numbers = []
        for i in numbers.split(delimiter):
            if i:
                if int(i) <= 1000:
                    num += int(i)
                if int(i) < 0:
                    negative_numbers.append(int(i))

        if negative_numbers:
            if len(negative_numbers) > 1:
                raise ValueError(f"negatives not allowed : {negative_numbers}")
            else:
                raise ValueError(f"negatives not allowed")

        return num
