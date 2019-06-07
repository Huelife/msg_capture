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

  for x in range(msg_length):
    if msg[x] in verbs:
      print("Slow down!")
    elif msg[x] in noun:
      print("Someone's full of themselves.")
    else:
      with open("words.txt","a") as fout:
        fout.write(msg[x] + "\n")

  with open("words.txt","a") as fout:
        fout.write("\n\n")

user_msg()

