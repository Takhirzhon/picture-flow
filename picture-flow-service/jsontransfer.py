import json
import redis

r = redis.Redis(host='redis-14795.c302.asia-northeast1-1.gce.cloud.redislabs.com', port=14795, db=0, username='default',password='d9VRpwCIqwzvK2vUJFqy81qFAQaqifEp',decode_responses=True)


# with open('./user.json', 'r') as file:
#     user_data = json.load(file)

# for user in user_data:
#     user_id = user['id']
#     r.hset(f'user:{user_id}', mapping=user)




# with open('./pictures.json', 'r') as file:
#     pictures_data = json.load(file)

# for picture_id, picture_info in pictures_data.items():
#     r.hset(f'picture:{picture_id}', mapping=picture_info)







# with open('./profilepictures.json', 'r') as file:
#     profilePictures = json.load(file)

# pipe = r.pipeline()

# for profile_picture_id, filename in profilePictures.items():
#     pipe.set(f'profilePictures:{profile_picture_id}', filename)

# pipe.execute()



# user_keys = r.keys('user:*')

# for user_key in user_keys:
#     user_data = r.hgetall(user_key)
#     email = user_data.get('email')
#     user_id = user_data.get('id')
    
#     if email and user_id:
#         r.set(f"email_to_id:{email}", user_id)

# print("Email to ID mappings have been created for existing users.")