def count_vowels_consonants(text):
    text = "I'm iron Man"
    text.lower()
    text.replace(" ","")
    text.replace("0","")
    text.replace("1","")
    text.replace("2","")
    text.replace("3","")
    text.replace("4","")
    text.replace("5","")
    text.replace("6","")
    text.replace("7","")
    text.replace("8","")
    text.replace("9","")
    vowel = text.count('a') + text.count('e') + text.count
    consonants = len(text) - vowels

    return{
        'vowels': vowels,
        'consonants': consonants,
    }