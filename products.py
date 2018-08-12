# 重複輸入：所以用到「迴圈」
# while True：適用於不知道會重複幾次的迴圈
# 兩個維度的清單，清單中還有清單
products = [] #清單，裝著輸入的商品
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    p = [] # 建立清單中的小清單
    p.append(name)
    p.append(price)  # 第10~12行，可以寫成 p = [name, price]
    products.append(p) # 把小清單裝入大清單中  # 第10~13行，可以寫成 products.append([name, price])  
print(products)

n = products[1][0] # products清單中第“０”格的第“０”
print(n)

for p in products:
    print(p[0], '的價格是', p[1])