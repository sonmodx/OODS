class translator:

    def deciToRoman( self,num):
        strc = ""
        while num >0 :
            while num-1000>=0 :
                num-=1000
                strc+="M"
            while num-900>=0 :
                num-=900
                strc+="CM"
            while num-500>=0 :
                num-=500
                strc+="D"
            while num-400>=0 :
                num-=400
                strc+="CD"
            while num-100>=0 :
                num-=100
                strc+="C"
            while num-90>=0 :
                num-=90
                strc+="XC"
            while num-50>=0 :
                num-=50
                strc+="L"
            while num-40>=0 :
                num-=40
                strc+="Xl"
            while num-10>=0 :
                num-=10
                strc+="X"
            while num-9>=0 :
                num-=9
                strc+="IX"
            while num-5>=0 :
                num-=5
                strc+="V"
            while num-4>=0 :
                num-=4
                strc+="IV"
            while num-1>=0 :
                num-=1
                strc+="I"
             
        return str(strc)
        ### Enter Your Code Here ###

    def romanToDeci(self,s):
        sum =0
        i =0
        while i < len(s) :
            if i < len(s)-1 and translator.translateRoman(s[i]) < translator.translateRoman(s[i+1]) :
                sum += translator.translateRoman(s[i+1]) - translator.translateRoman(s[i])
                i+=1
            else :
                sum += translator.translateRoman(s[i])
            i+=1
        return sum
        ### Enter Your Code Here ###

    def translateRoman(ch):
        if ch =='I':
            return 1
        elif ch =='V':
            return 5
        elif ch =='X':
            return 10
        elif ch =='L':
            return 50
        elif ch=='C':
            return 100
        elif ch=='D':
            return 500
        elif ch=='M':
            return 1000
        else :
            return


num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))