class StringCalculator:

    def add(self, numbers: str) -> int:

        if not numbers:
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[3:]

        numbers = numbers.replace("\n", delimiter)
        num = 0
        negative_numbers = []
        for i in numbers.split(delimiter):
            if i:
                num += int(i)
                if int(i) < 0:
                    negative_numbers.append(int(i))
                    
        if negative_numbers :
            if len(negative_numbers) > 1:
                raise ValueError(f"negatives not allowed : {negative_numbers}")
            else:
                raise ValueError(f"negatives not allowed")

        return num
