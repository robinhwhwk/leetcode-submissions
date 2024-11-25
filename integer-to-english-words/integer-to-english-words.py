class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
            
        postfix = ["" , "Thousand", "Million", "Billion"]
        ones_strings = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }

        teens_strings = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        
        tens_strings = {
            1: "Ten",
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
        res = ""
        index = 0
        while num > 0:
            current_string = ""
            current_number = num % 1000
            ones = current_number % 10
            tens = (current_number % 100) // 10
            hundreds = current_number // 100
            if tens == 1:
                tens = teens_strings[current_number % 100]
                current_string = tens + " " + current_string
            else:
                if ones:
                    ones = ones_strings[ones]
                    current_string = ones + " " + current_string
                if tens:
                    tens = tens_strings[tens]
                    current_string = tens + " " + current_string
            if hundreds:
                hundreds = ones_strings[hundreds]
                current_string = hundreds + " Hundred " + current_string

            num = num // 1000
            print("current_string:", current_string)
            print("current_number:", current_number)
            print("num:", num)
            if current_number:
                print("adding postfix:", postfix[index])
                current_string += postfix[index]
            index += 1
            if current_string and index == 1:
                res = current_string
            elif current_string:
                res = current_string + " " + res
        res = res[:len(res) - 1]
        return res

        