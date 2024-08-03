class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following +=1
        user.followers +=1


user1 = User(1, 'Vic')
user2 = User(2, 'Bob')
print(user1, user1.id, user1.name, user1.followers)

user1.follow(user2)
print(user1.following)
print(user2.followers)