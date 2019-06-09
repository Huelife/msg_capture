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
  y = 0

  for x in range(msg_length):
    if msg[y] in verb:
      print("Slow down!")
    elif msg[y] in adverb:
      print("")
    elif msg[y] in noun:
      print("Someone's full of themselves.")
    elif msg[y] in pronoun:
      print("")
    elif msg[y] in adjective:
      print("")
    elif msg[y] in preposition:
      print("")
    elif msg[y] in conjunction:
      print("")
    elif msg[y] in interjection:
      print("")
    else:
      with open("words.txt","a") as fout:
        fout.write(msg[y] + "\n")
    y += 1

  with open("words.txt","a") as fout:
    fout.write("\n")

user_msg()
