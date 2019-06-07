#msg_capture.py: Replies to user input and stores unknown words

#sentence parts variables
verb = ["run","walk","jog","sprint"]
adverb = []
noun = []
pronoun = []
adjective = []
preposition = []
conjunction = []
interjection = []

word_check = {}

#function to capture user input and split to parts
def user_msg():
  msg = input("Hi!").lower().split()
  msg_length = len(msg)

  for x in range(msg_length):
    if msg[x] in verb:
      print("Slow down!")
    elif msg[x] in adverb:
      print("")
    elif msg[x] in noun:
      print("Someone's full of themselves.")
    elif msg[x] in pronoun:
      print("")
    elif msg[x] in adjective:
      print("")
    elif msg[x] in preposition:
      print("")
    elif msg[x] in conjunction:
      print("")
    elif msg[x] in interjection:
      print("")
    else:
      with open("words.txt","a") as fout:
        fout.write(msg[x] + "\n")

  with open("words.txt","a") as fout:
    fout.write("\n\n")

user_msg()

