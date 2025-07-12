from art import logo, vs
from data import data
from random import choice
import os
#Generate a random intger and returns the coresopending dic from data list.
def generate_candidate(data):
    candidate = choice(data)
    return candidate


#print the info of each candidate.
def print_info(A_cand, B_cand):
    if A_cand["description"][0].lower() in "aeiou":
        print(f"Compare A: {A_cand["name"]}, an {A_cand["description"]}, from {A_cand["country"]}.")
    else:
        print(f"Compare A: {A_cand["name"]}, a {A_cand["description"]}, from {A_cand["country"]}.")
    print(vs)
    if B_cand["description"][0].lower() in "aeiou":   
        print(f"against B: {B_cand["name"]}, an {B_cand["description"]}, from {B_cand["country"]}.")
    else:
        print(f"against B: {B_cand["name"]}, a {B_cand["description"]}, from {B_cand["country"]}.")
        
        
#Compare who got more followers.
def compare(A_cand, B_cand):
    if A_cand["follower_count"] > B_cand["follower_count"]:
        return 'a'
    elif A_cand["follower_count"] < B_cand["follower_count"]: 
        return 'b'
    else:
        return 0
    
    
#Keep track of the player score and determine whether they have lost or not.
def score(guess, answer, curr_score):
    if answer == guess:
        curr_score += 1
        return curr_score
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {curr_score}")
        return False
        
   
end_game = False
A_candidat = generate_candidate(data)
curr_score = 0
while not end_game:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    if curr_score != 0:
        print(f"You're right! Current score: {curr_score}")
    B_candidat = generate_candidate(data)
    print_info(A_candidat, B_candidat)
    answer = compare(A_candidat, B_candidat)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    curr_score = score(answer, guess, curr_score)
    if not curr_score:
        end_game = True
    A_candidat = B_candidat
    


      
