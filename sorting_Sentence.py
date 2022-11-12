class Solution:
    def sortSentence(self, s: str) -> str:
        arr = [None] * 9
        ind = 0
        temp = ""
        while ind < len(s):
            if '0' <= s[ind] <= '9':
                num = int(s[ind]) - 1
                arr[num] = temp
                temp = ""
                ind += 2
            else:
                temp += s[ind]
                ind += 1
        i = 0
        sentence = ""
        try:
            while arr[i] != None:
                sentence += str(arr[i])

                if arr[i+1] != None:
                    sentence += " "

                i += 1
        except:
            pass
        return sentence
