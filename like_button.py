user1_profile = [2, 1, 5, 3, 6, 4]

def like (user, new_object):
    user.append(new_object[0])
    user_profile_sum = sum(user)
    user_likes = len(user)
    user_like_average = user_profile_sum / user_likes
    return user_like_average

def set_object(object_value):
    object_value.insert(0, int(input('Input Value of Liked Object: ')))
    return object_value

new_object = [0]
while new_object[0] != 10000:
    set_object(new_object)
    print (like(user1_profile, new_object))
    print (user1_profile)
