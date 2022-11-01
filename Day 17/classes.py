class User:
    #pass | to leave this empty for now but remove indent errors
    def __init__(self, user_id, username): #self is the object itself being created
        print("new user being created...") #this statement gets executed every time an object gets called in this class
        self.id = user_id
        self.username = username
        self.followers = 0 #initializing it as 0 for the object that is made
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1




user_1 = User("001", "samuel")

print(user_1.id)

user_2 = User("002", "jack")

# print(user_1.followers)

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)