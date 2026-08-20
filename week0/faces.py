emo = input("write your emoticon")
def comvert(emo):
    emo = emo.replace(":)","🙂")
    emo = emo.replace(":(","🙁")
    return(emo)
print(comvert(emo))

