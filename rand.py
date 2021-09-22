target_profile = "prevailinggamers"

from instaloader import Instaloader, Profile
loader = Instaloader()

profile = Profile.from_username(loader.context, target_profile)

num_followers = profile.followers
print('Total Followers ' + str(profile.followers))
total_num_likes = 0
total_num_comments = 0
total_num_posts = 0

num_accounts = profile.mediacount
#print('Total Posts '+ str(num_accounts))

counter = 0;
for post in profile.get_posts():
    total_num_likes += post.likes
    counter = counter + 1;
    if counter == 10:
        break
    #total_num_comments += post.comments
    #total_num_posts += 1

print(total_num_likes)
print(total_num_likes/num_accounts)
