#Letter counter
def letter_counter(word):
    list1=list(word)
    list2=[]
    for letter in list1:
        list2.append(letter)
    return len(list2)

print(letter_counter('Hello'))
#Results 5