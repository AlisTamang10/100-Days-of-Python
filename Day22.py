# Create a program capable of displaying Questions to the user like KBC
# Use list data-type to store the questions and their correct answers
# Display the final amount the person takes home post game-play

questions = [
    "What's the capital city of Nepal ?",
    "Who is the light of Asia ?",
    "Who won the Championship League 2024 ?"   
]

choices = [
    ["A) Delhi","B) Dhaka","C) Kathmandu", "D) Lalitpur"],
    ["A) Gandhi", "B) Buddha", "C) Bhanu Bhakta", "D) Narendra Modi"],
    ["A) Reald Madrid", "B) Manchester City", "C) Barcelona", "D) Manchester United"]
]

answers = ["C","B","A"]
prizes = ['1 Cr','2 Cr',' 3 Cr']
total_amount = 0

while True:
    for i in range(len(questions)):
        print("Question",i+1,questions[i])
        for choice in choices[i]:
            print(choice)
            
        ans = input("Enter your choice (A/B/C/D): ")
        
        if ans== answers[i]:
            total_amount = prizes[i]
            print("Congrats !! you won", prizes[i])
            
        else:
            print("Sorry You lost the game.")
            break
        
    print("Your total prize is", total_amount)
    
    retry = input("Do you want to play again ?(Y/N):")
    
    if retry != "Y":
        break

