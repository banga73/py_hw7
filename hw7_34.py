phrase = "пара-ро-рам рам-пим-ппамё па-ру-па-да"
sounds = ('а', 'я', 'о', 'ё', 'у', 'ю', 'ы', 'и', 'э', 'е')
words_list = phrase.split()
sounds_num = []
for j in range(len(words_list)):
    sounds_num.append(0)
    for i in words_list[j]:
        if (i in sounds):
            sounds_num[j] += 1
print("true" if len(set(sounds_num)) == 1 else "false")