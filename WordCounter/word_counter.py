#Word_counter
def word_counter(word):
    list1=word.split()
    list2=[]
    for letter in list1:
        list2.append(letter)
    return len(list2)

print(word_counter('Hello, How are you?'))
#Results 4