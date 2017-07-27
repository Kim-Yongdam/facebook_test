import json
import codecs

f_file_in = open("my_posts.txt", "r")

log_count = 1

for line in f_file_in:
    post = json.loads(line)
    print(post)
    #print(post, file=f_file_out)
    #print("log No.%d" % log_count, end=" ", file=f_file_out)
    #log_count = log_count + 1