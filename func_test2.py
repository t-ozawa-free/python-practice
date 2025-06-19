def postTaxPrice(price):
    ans = price * 1.1
    return ans

for i in range(11):
    print("値段を入力してください（", i, "/10）")
    m = int(input())
    print("税抜き：", m, "円", "税込み：",postTaxPrice(m), "円")