user1_profile = [2, 1, 5, 3, 6, 4]

def like (user, new_object):
    user.append(new_object[0])
    user_profile_sum = sum(user)
    user_likes = len(user)
    user_like_average = user_profile_sum / user_likes
    return user_like_average

def set_object(object_value):
    object_value.insert(0, int(input('Input Value of Liked Object: ')))
    x = 1
    print ('The Value of Object ', x, ' is:', object_value[0])
    x += 1
    return object_value

def create_liked_object():
    new_object = [0]
    return new_object
    

new_object = [0]
while new_object[0] != 10000:
    set_object(new_object)
    print (like(user1_profile, new_object))
    print (user1_profile)
