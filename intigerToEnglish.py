class Solution:
    def __init__(self):
        self.power = 0
        self.english = ""
        self.is_zero = True
    def numberToWords(self, num: int) -> str:
        if self.is_zero and num == 0:
            return "Zero"
        if num  < 1000 and self.power == 0:
            self.english += self.thousandsToWords(num, self.power)

            return self.english[:-1]
        elif num < 1000:
            self.is_zero = False
            self.english += self.thousandsToWords(num, self.power)
            self.power -= 1


        else:
            self.power += 1
            self.numberToWords(num // 1000)
            self.numberToWords(num % 1000)
            return self.english[:-1]



    def thousandsToWords(self, number, power):
        single_digits = ["", "One ", "Two ", "Three ", "Four ",
            "Five ", "Six ", "Seven ", "Eight ", "Nine " ]
        two_digits = ["Ten ", "Eleven ",  "Twelve ",
            "Thirteen ",  "Fourteen ", "Fifteen ", "Sixteen ",
            "Seventeen ", "Eighteen ", "Nineteen "]
        ten_multiple = ["","","Twenty ",
                              "Thirty ", "Forty ",   "Fifty ",
                              "Sixty ",  "Seventy ", "Eighty ",
                              "Ninety "]
        ten_power = ["", "Thousand ", "Million ", "Billion ","Trillion "]
        english = ""
        if number // 100 != 0:
            english += single_digits[number//100] + "Hundred "

        number %= 100
        if number // 10 == 1:

                english += two_digits[number % 10]

        else:
            english += ten_multiple[number // 10] + single_digits[number % 10]
        if english:
            english += ten_power[power]
        return english
            