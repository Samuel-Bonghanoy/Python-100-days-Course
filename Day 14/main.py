import random
import os
import data
import art

#Gets the initial two topics for the start of the game
def get_initial_topics():
    topic_a = data.data[random.randint(0, len(data.data) - 1)]
    topic_b = data.data[random.randint(0, len(data.data) - 1)]
    return topic_a, topic_b

#Prints out the details of the topic
def print_details_a(topic):
    details = f""
    ctr = 1
    #adds the details of the topic to the details variable that will be printed after the loop
    for detail in topic:
        if not detail == 'follower_count':
            if ctr == 1:
                details += topic[detail] + ', '
                ctr += 1
            elif ctr == 2:
                details += 'a ' + topic[detail] + ', '
                ctr += 1
            elif ctr == 3:
                details += 'from ' + topic[detail] + '.'

    print(f"Compare A: {details}")

def print_details_b(topic):
    details = f""
    ctr = 1
    #adds the details of the topic to the details variable that will be printed after the loop
    for detail in topic:
        if not detail == 'follower_count':
            if ctr == 1:
                details += topic[detail] + ', '
                ctr += 1
            elif ctr == 2:
                details += 'a ' + topic[detail] + ', '
                ctr += 1
            elif ctr == 3:
                details += 'from ' + topic[detail] + '.'

    print(f"Against B: {details}")

def compare_topics(streak, user_choice, topic_a, topic_b):
    if topic_a['follower_count'] > topic_b['follower_count']:
        if user_choice == 'A':
            os.system('cls||clear')
            return int(streak + 1)
        else:
            os.system('cls||clear')
            print(f"Sorry, that's wrong. Final score: {streak}")
            return 0
    elif topic_b['follower_count'] > topic_a['follower_count']:
        if user_choice == 'B':
            os.system('cls||clear')
            return int(streak + 1)
        else:
            os.system('cls||clear')
            print(f"Sorry, that's wrong. Final score: {streak}")
            return 0


def get_new_topic(topic_a, topic_b):
    temp = topic_b
    topic_b = data.data[random.randint(0, len(data.data) - 1)]
    while topic_b == temp:
        topic_b = data.data[random.randint(0, len(data.data) - 1)]
    topic_a = temp
    return topic_a, topic_b

def game():
    streak_alive = True
    streak = 0
    temp_streak = streak
    #Initializes the player's streak as 0
    while streak_alive: 
        #Lets the player keep going as long as their streak is still ongoing
        print(art.logo) 
        if temp_streak > 0:
            print(f"You're right! Current score: {temp_streak}.")

        topic_a, topic_b = get_initial_topics() 
        #Gets the initial topics to be compared

        print_details_a(topic_a)
        #Prints the details for Topic A

        print(art.vs) 
        print_details_b(topic_b)
        #Prints the details for Topic A

        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        #Asks the user for their choice
        
        streak = compare_topics(temp_streak, user_choice, topic_a, topic_b)
        #Sees if the user is correct and returns true or false value to continue game or end it

        temp_streak = streak

        if temp_streak == 0:
            streak_alive = False
        else:
            streak_alive = True
        #Sees if the user was correct and continues the game accordingly

        get_new_topic(topic_a, topic_b)
        #Sets topic A as the previous topic B, and gets a new topic for topic B

game()

