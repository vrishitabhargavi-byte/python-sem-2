words = ["mass", "as", "hero", "superhero"]

result = []

for i in range(len(words)):
  for j in range(len(words)):
    if i!=j:
      if words[i] in words[j]:
             result.append(words[i])
             break

print("Matching words are:",result)