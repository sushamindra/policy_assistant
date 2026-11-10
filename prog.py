question = "What is your name"
q2 = "What is my name"

w1 = question.lower().split()
w2 = q2.lower().split()

ans = (set(w1) & set(w2))
print(ans)