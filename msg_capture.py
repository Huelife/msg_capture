#msg_capture.py: Replies to user input and stores unknown words

#sentence parts variables
verb = ["run","walk","jog","sprint"]
adverb = []
noun = []
pronoun = []
adjective = []
prepositon = []
conjunction = []
interjection = []

#function to capture user input and split to parts
def user_msg():
  msg = input("Hi!").lower().split()
  msg_length = len(msg)
