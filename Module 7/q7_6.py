"""
Quiz 7
Question 6
Top 10 Words

Calculate the top 10 most frequent words in a given block of text.
You can assume that no punctuation other than spaces and periods will be used.
"""

text = "contented get distrusts certainty nay are frankness concealed ham. \
on unaffected resolution on considered of. no thought me husband or colonel \
forming effects. end sitting shewing who saw besides son musical adapted. \
contrasted interested eat alteration pianoforte sympathize was. he families \
believed if no elegance interest surprise an. it abode wrong miles an so delay \
plate. she relation own put outlived may disposed. projecting surrounded \
literature yet delightful alteration but bed men. open are from long why cold. \
if must snug by upon sang loud left. as me do preference entreaties compliment \
motionless ye literature. day behaviour explained law remainder. produce can \
cousins account you pasture. peculiar delicate an pleasant provided do perceive. \
still court no small think death so an wrote. incommode necessary no it behaviour \
convinced distrusts an unfeeling he. could death since do we hoped is in. exquisite \
no my attention extensive. the determine conveying moonlight age. avoid for see \
marry sorry child. sitting so totally forbade hundred to. to sure calm much most \
long me mean. able rent long in do we. uncommonly no it announcing melancholy an in. \
mirth learn it he given. secure shy favour length all twenty denote. he felicity no \
an at packages answered opinions juvenile. attended no do thoughts me on dissuade \
scarcely. own are pretty spring suffer old denote his. by proposal speedily mr \
striking am. but attention sex questions applauded how happiness. to travelling \
occasional at oh sympathize prosperous. his merit end means widow songs linen known. \
supplied ten speaking age you new securing striking extended occasion. sang put paid \
away joy into six her. am increasing at contrasted in favourable he considered \
astonished. as if made held in an shot. by it enough to valley desire do. mrs chief \
great maids these which are ham match she. abode to tried do thing maids. doubtful \
disposed returned rejoiced to dashwood is so up. procuring education on consulted \
assurance in do. is sympathize he expression mr no travelling. preference he he at \
travelling in resolution. so striking at of to welcomed resolved. northward by \
described up household therefore attention. excellence decisively nay man yet \
impression for contrasted remarkably. there spoke happy for you are out. fertile \
how old address did showing because sitting replied six. had arose guest visit going \
off child she new. affronting discretion as do is announcing. now months esteem \
oppose nearer enable too six. she numerous unlocked you perceive speedily. affixed \
offence spirits or ye of offices between. real on shot it were four an as. absolute \
bachelor rendered six nay you juvenile. vanity entire an chatty to. yourself required \
no at thoughts delicate landlord it be. branched dashwood do is whatever it. farther \
be chapter at visited married in it pressed. by distrusts procuring be oh frankness \
existence believing instantly if. doubtful on an juvenile as of servants insisted. \
judge why maids led sir whose guest drift her point. him comparison especially \
friendship was who sufficient attachment favourable how. luckily but minutes ask \
picture man perhaps are inhabit. how her good all sang more why. pasture he invited \
mr company shyness. but when shot real her. chamber her observe visited removal six \
sending himself boy. at exquisite existence if an oh dependent excellent. are gay \
head need down draw. misery wonder enable mutual get set oppose the uneasy. end why \
melancholy estimating her had indulgence middletons. say ferrars demands besides her \
address. blind going you merit few fancy their."


def word_freq(string):
    d = {}
    strip = string.replace(".", "")
    lower = strip.lower()
    words = lower.split(" ")

    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d


def top_num(d, num):
    s = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    top = []
    for y in range(0, num):
        top.append(s[y])
    return top


x = word_freq(text)
print(top_num(x, 10))
