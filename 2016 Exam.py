#Using list as a variable name #1
#length is not a function, len is #3&4&7
#Operator lst is never referenced within function definition #all lines
#Should be ** instead of * #5
#Median calculations assume list is sorted #4&7
#None is returned, not the area #9
#The function prints instead of returns #5&8
#Should be length of list - 1 for median if odd number of elements #7
#set is never defined #3&4&7

class Prof:
    DRESS_SENSES = ['over', 'smart', 'borderline', 'omg']
    def __init__(self, aloofness, dress_sense):
        #if not self.aloofness.isnumeric():\
            #raise ValueError
        #if self.aloofness not in range(11):
            #if self.aloofness > 10:
                #self.aloofness = 10
            #else:
                #self.aloofness = 0
        self.aloofness = aloofness # on a scale of (grounded) 1 to 10 (aloof)
        if dress_sense in Prof.DRESS_SENSES:
            self.dress_sense = dress_sense
        else:
            self.dress_sense = 0
    def __repr__(self):
        return("{} {}".format(self.aloofness, self.dress_sense))

print(Prof(5.2, Prof.DRESS_SENSES[1]))

'''
The object p is assigned to an object of class Prof with aloofness = f and dress_sense = 0
(since "wtf" isn't in DRESS_SENSES). Therefore p.dress_sense returns 0 hence p.aloofness returns
f(p.dress_sense) = f(0). This then calls our function f(x) with x = 0 which gives a return value of 3.
'''

'''
<!DOCTYPE html>
<html>
<body>
<h1>Question 3 [10 marks]</h1>
<p>Write HTML code that would best represent this page (before you have written on it!).</p>
</body>
</html>
'''

'''
The action, completing q takes O(1) time to complete. Scanning all questions means the program has to look at all n
questions so this action will take O(n) time to complete. So our current time for one scan and completion is O(1) + O(n)
which simplifies to O(n) as we only care about the biggest term. However, we have to do this action n times because
there are n questions to answer. Thus our complexity is O(n) times O(n) or O(n**2)
'''

'''
This is very similar to bubble sort.
'''

def count_repeats(input):
    import string

    for p in string.punctuation:
        input = input.replace(p, ' ')
    s = input.split()

    count = len(s)
    dic = {}

    for i in range(1, count):
        key = (s[i-1], s[i])
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1

    result = []
    print(dic.items())
    for k, v in dic.items():
        if v > 1:
            result += tuple([k])
    return result
print(count_repeats("Ann 'eats at Joe's. Ann eats :;apples. hello bob hello bob hello bob"))