#understanding slicing concept 

str= "GulabJamun"

firstHalf= str[0:5] #Gulab
trialFirstHalf= str[ :5] #Gulab

print(firstHalf)
print(trialFirstHalf)

secondHalf= str[5:10] #Jamun
trialSecondHalf= str[5: ] #Jamun

print(secondHalf)
print(trialSecondHalf)