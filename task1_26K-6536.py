depth = int(input("Enter security stage depth (min 4): "))
while depth < 4:
    print("Depth must be at least 4.")
    depth = int(input("Enter security stage depth (min 4): "))

seq = [2]

while len(seq) < depth:
    i = len(seq) - 1
    if i % 2 == 0:
        seq.append(seq[-1] + 3)
    else:
        seq.append(seq[-1] * 2)

print("Firewall Code Generated:", *seq[:-1], "[ ? ]")
guess = int(input("Enter the override token: "))

if guess == seq[-1]:
    print("ACCESS GRANTED: Firewall bypassed successfully! Full sequence:", *seq)
else:
    print("ACCESS DENIED: Alarm triggered! Expected value:", seq[-1])
