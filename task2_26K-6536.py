depth = int(input("Enter Frequency cycle depth :  "))
while depth < 4:
  depth = int(input("re enter security depth (min 4) "))

seq = [2]
while len(seq)<depth:
  seq.append((seq[-1] * 2 + 1))
print(*seq[:-1], "[ ? ]" )

guess = int(input("Enter guess to access the security : "))
if guess != seq[-1]:
  print("SHIELD UNSYNCHRONIZED: Plasma wave not deflected!")
else:
  print("SHIELD SYNCHRONIZED: Plasma wave deflected!")
