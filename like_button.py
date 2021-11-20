user1_profile = [2, 1, 5, 3, 6, 4]

def like (user, new_object):
    user.append(new_object[0])
    user_profile_sum = sum(user)
    user_likes = len(user)
    user_like_average = user_profile_sum / user_likes
    return user_like_average

new_object = [0]
while new_object[0] != 1000:
    new_object.insert(0, int(input('Input Number:')))
    print (like(user1_profile, new_object))
