question = ["where is bhubaneswar" , "How many bones are there in human body", "who is the pm of India"]
que = input("Please ask question?")
answer = input("Please give your answer")

for i in range(len(question)):
    if(question[i] == "where is bhubaneswar" and answer == "odisha"):
        print("You have won 1 Lkah ruppees. Congratulations!!")
    if(question[i] == "How many bones are there in human body" and answer == 206):
        print("You have won 10 lakhs")
    if(question[i] == "who is the pm of India" and answer == "Narendra Modi"):
        print("You have 50 lakh ruppees. Congratulations!!")