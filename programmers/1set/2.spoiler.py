messages = "Hello World KIM JIWOO Hello"
spoiler_ranges = [[0, 3], [6, 7]]

n = len(messages)
spoiler_check_list = [False] * n

for start, end in spoiler_ranges:
  for j in range(start, end + 1):
    if start <= j <= end:
      spoiler_check_list[j] = True

public_words = set()
spoiler_words = set()

i = 0

while i < n:
  if messages[i] == " ":
    i += 1
    continue
  
  start = i

  while i < n and messages[i] != " ":
    i += 1

  end = i - 1

  # for j in range(start, end + 1):
  #   if spoiler_check_list[j]:
  #     spoiler_words.add(messages[start:end + 1])
  #     break
  #   else:
  #     public_words.add(messages[start:end + 1])
  
  has_spoiler = any(spoiler_check_list[start:end + 1])
  
  if has_spoiler:
    spoiler_words.add(messages[start:end + 1]) 
  else:
    public_words.add(messages[start:end + 1])


print("Spoiler Words:", spoiler_words)
print("Public Words:", public_words)

print("Result Count:", spoiler_words - public_words)