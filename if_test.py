score = int(input("あなたの点数を教えて(0～100)"))

if (score > 80) & (score <= 100):
    print("なかなかすごいね！")
elif (score > 60) & (score <= 80):
    print("まぁまぁだね")
elif (score >= 0) & (score <= 60):
    print("ダメダメだね・・・")
else:
    print("1～100だって言ってるだろ！")
