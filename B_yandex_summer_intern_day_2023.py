t = int(input())
words = [input() for i in range(2*t)]

for i in range(t):

    status = ""
    word_a = words[2*i]
    word_b = words[2*i+1]

    letters_changer = dict()
    reversed_changer = dict()

    for j in range(len(word_a)):

        original_letter = word_a[j]
        changed_letter = word_b[j]

        if letters_changer.get(original_letter):
            if letters_changer[original_letter] != changed_letter:
                status = "Error"
                break
        elif reversed_changer.get(changed_letter):
            if reversed_changer[changed_letter] != original_letter:
                status = "Error"
                break
        else:
            letters_changer[original_letter] = changed_letter
            reversed_changer[changed_letter] = original_letter
    
    if not status:
        print("YES")
    else:
        print("NO")


