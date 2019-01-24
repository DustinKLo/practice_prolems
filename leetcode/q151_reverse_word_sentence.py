
def reverse_words_in_sentence(sentence):
    ans = ''
    word = ''

    for i in range(len(sentence)):
        if i == len(sentence) - 1:
            word = sentence[i] + word
            ans = ans + ' ' + word
            break

        if sentence[i] != ' ':
            word = sentence[i] + word
        else:
            ans = ans + ' ' + word
            word = ''

    return ans[1:]


if __name__ == '__main__':
    print(reverse_words_in_sentence('hello there dustin'))
    print(reverse_words_in_sentence('abcdefghijklmnopqrstuvwxyz'))
    print(reverse_words_in_sentence('00000000000000000000000000000000000000000000000000001'))

