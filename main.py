import string
from collections import Counter
import matplotlib.pyplot as plt


text= open('read.txt',encoding='utf-8').read()
lower_case=text.lower()
cleand_text= lower_case.translate(str.maketrans('','',string.punctuation))
tokenized_words=cleand_text.split()
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words=[]
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

#print(final_word)

# 1) Check if the word in the final word list is also present in emotion.txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split

# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list
emotion_list = []
positive_list=[]
negative_list=[]
with open('emotion.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)
with open("positive_negative_sentiment.txt",'r') as file:
    for line1 in file:
        clear_line1=line1.replace("\n","")
        negative , positive=clear_line1.split(":")
        #print("negative is : "+negative+" positive is : "+positive)
        positive_list.append(positive)
        negative_list.append(negative)
#print(emotion_list)
#print(negative_list)
#print(positive_list)
final_list_positive=[]
final_list_negative=[]
for i in range(0,len(emotion_list)):
        if emotion_list[i] in positive_list:
            final_list_positive.append(emotion_list[i])
        else:
            final_list_negative.append(emotion_list[i])
#print(final_list_negative)
#print(final_list_positive)
#################################################################################################################
w1=Counter(emotion_list)
print(w1)
#fig, ax1=plt.subplots()
#ax1.bar(w1.keys(),w1.values())
#fig.autofmt_xdate()
#plt.savefig("graph.png")
#plt.show()

#Plot of the positive emotion###################################################################################
#w2=Counter(final_list_positive)
#print(w2)
#fig, ax1=plt.subplots()
#ax1.bar(w2.keys(),w2.values())
#fig.autofmt_xdate()
#plt.savefig("postiveEmotion.png")
#plt.show()

#Plot of the positive emotion###########################################################################
#w3=Counter(final_list_negative)
#print(w3)
#fig, ax1=plt.subplots()
#ax1.bar(w3.keys(),w3.values())
#fig.autofmt_xdate()
#plt.savefig("negativeEmotion.png")
#plt.show()
#########################################################################################################
counter1=Counter({'positive':0,'negative':0})
counter1['positive']=len(final_list_positive)
print(final_list_negative)
print(final_list_positive)
counter1['negative']=len(final_list_negative)
print(counter1)
fig, ax1=plt.subplots()
ax1.bar(counter1.keys(),counter1.values())
fig.autofmt_xdate()
plt.savefig("negativePositiveEmotion.png")
plt.show()