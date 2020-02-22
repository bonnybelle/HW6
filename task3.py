# 3. Дан текст - найти все заглавные буквы и объединить их в слово.
# 'Help ELephant learn LOops. While's and fOrs. RLD!'

s = "Help ELephant learn LOops. While's and fOrs. RLD!"
for ch in s:
    word = ch if ch.isupper() else ""
    print(word, end="")


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in s:
    word = i if i in alphabet else ""
    print(word, end="")
