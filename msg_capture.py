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

#function to capture and split user input, and decide what to do with it
def user_msg():
  msg = input("Hi!").lower().split()
  msg_length = len(msg)
  y = 0
  
  #checking user input, creating reply, and exporting unknown strings
  for x in range(msg_length):
    if msg[y] in verb:
      reply = "Slow down!"
    elif msg[y] in adverb:
      reply = ""
    elif msg[y] in noun:
      reply = "Someone's full of themselves."
    elif msg[y] in pronoun:
      reply = ""
    elif msg[y] in adjective:
      reply = ""
    elif msg[y] in preposition:
      reply = ""
    elif msg[y] in conjunction:
      reply = ""
    elif msg[y] in interjection:
      reply = ""
    else:
      with open("words.txt","a") as fout:
        fout.write(msg[y] + "\n")
    y += 1

  with open("words.txt","a") as fout:
    fout.write("\n")
    
  print(reply)

user_msg()
