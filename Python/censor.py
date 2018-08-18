def censor(text, word):
  words = text.split()
	
  for i, value in enumerate(words):
    if value == word:
      words[i] = "*" * len(value)
  words = " ".join(words)
  return words
  
  
print(censor("this hack is wack hack", "hack"))
