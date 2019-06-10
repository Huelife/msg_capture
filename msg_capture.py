#msg_capture.py: Replies to user input and stores unknown words

#sentence parts variables
verb = ["run","walk","jog","sprint"]
noun = ["i","my","mine","me","i'm","im"]
pronoun = ["he","him","his","her","she","them","there","it","you","your",
           "they","we","us","our","there","theyre","they're","mines","mine",
           "ours","yours","theres","there's","theirs"]
preposition = ["aboard","behind","during","about","below","except","above",
               "beneath","for","across","beside","from","after","besides",
               "in","against","between","inside","along","beyond","into",
               "among","but","like","around","by","near","at","concerning",
               "of","before","down","off","on","throughout","until","out",
               "till","up","over","to","upon","past","toward","with","since",
               "under","within","through","underneath","without","til"]
greet = ["hi","hey","yo","hello","sup","greetings"]

adverb = []
adjective = []
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
    if msg[y] in greet_day:
      reply = msg[y] + "!"
    elif msg[y] in verb:
      reply = "Slow down!"
    elif msg[y] in adverb:
      reply = ""
    elif msg[y] in noun:
      reply = "Someone's full of themselves."
    elif msg[y] in pronoun:
      reply = "Does {} have a name?".format(msg[y])
    elif msg[y] in adjective:
      reply = ""
    elif msg[y] in preposition:
      reply = "{} where?".format(msg[y])
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
