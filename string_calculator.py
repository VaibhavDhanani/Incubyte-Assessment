import re


class StringCalculator:

    def __init__(self) -> None:
        self.__add_called_count = 0

    def get_add_called_count(self) -> int:
        return self.__add_called_count

    def add(self, numbers: str) -> int:
        self.__add_called_count += 1

        if not numbers:
            return 0

        delimiters = []
        start = 0
        if numbers.startswith("//"):
            i = 2
            while i < len(numbers) and numbers[i] != "\n":
                if numbers[i] == "[":
                    i += 1
                    deli = ""
                    while numbers[i] != "]":
                        deli += numbers[i]
                        i += 1
                    delimiters.append(deli)
                    i += 1
                else:
                    deli = numbers[i]
                    delimiters.append(deli)
                    i += 1
                    break
            start = i + 1

        else:
            delimiters = [","]

        numbers = numbers[start:]
        numbers = numbers.replace("\n", delimiters[0])

        num = 0
        negative_numbers = []
        patterns = "|".join(map(re.escape, delimiters))
        for i in re.split(patterns, numbers):
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
