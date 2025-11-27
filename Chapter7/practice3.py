# Write a function that takes a string and returns the count of vowels and
# consonants separately.

def countVowConso(userInput):

    #define vowels
    vowels= "aeiouAEIOU"

    countVowel= 0
    countConsonants= 0

    #SAUMYA123 
    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowel= countVowel+1
            else:
                countConsonants+=1

    return countVowel, countConsonants


# Function Call 

vowels, consonants= countVowConso("Saumya Singh")

print(vowels, consonants)
print(vowel)