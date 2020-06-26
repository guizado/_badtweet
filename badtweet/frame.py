import tweepy
import frame_cred
from time import sleep
from templates import TemplateProccessor
from templates import cleanText
from templates import Library


def auth():
	auth = tweepy.OAuthHandler(frame_cred.consumer_key, frame_cred.consumer_secret)
	auth.set_access_token(frame_cred.token, frame_cred.token_secret)
	return auth


lib = Library("lib.json", "lib_q.json")
retry = 1

class Listener(tweepy.streaming.StreamListener):

	def __init__(self):
		self.api = tweepy.API(auth())


	def on_status(self, status):
		'''Called when a tweet containing "_badtweet" is found'''
		reply_id = status.in_reply_to_status_id
		screen_name = status.user.screen_name

		if reply_id != None:
			text = cleanText(self.api.get_status(reply_id).text)
			if len(text) > 0:
			    print("[TWEET DETECTED]")
			    t = lib.getTemplate()
			    TemplateProccessor(text, t).proccess(0, True)
			    media = self.api.media_upload("sample-out/out0.jpg").media_id
			    self.api.update_status('@'+screen_name, in_reply_to_status_id=status.id, media_ids=[media])
		return True


	def on_error(self, status):
		if status == 420:
			print("[ERROR 420 CUT STREAM]")
			return False
		print(status)



class ReplyStreamer():

	def __init__(self):
		self.listener = Listener()

	def live(self):
		#Live search for tweets with "_badtweet"
		retry = 1
		print("[STREAM IS LIVE]")
		stream = tweepy.streaming.Stream(auth(), self.listener)
		stream.filter(track=["_badtweet"])


while True:
	ReplyStreamer().live()
	sleep(15*retry)

