# 作業系統模組（第五步驟）
import os # operating system，標準函式庫中
# path 路徑； isfile 檢查檔案在不在

products = [] #先產生空清單
if os.path.isfile('products.csv'): # 檢查'products.csv'是否與本程式('product.py')在同一資料夾中
    print('找到檔案了！')
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue  # continue跟break一樣只能寫在迴圈(第5~11行)裡。 continue就是跳到下一迴的意思
            name, price = line.strip().split(',')
            # name = s[0]   price = s[1]
            # strip 去除 \n 還有 前後的空格
            # split 切割，()裡是切割的標記，切割完是清單[]
            products.append([name, price])
    print(products)

else:
    print('沒找到檔案！')

# 讓使用者輸入（第一步驟）
# 重複輸入：所以用到「迴圈」
# while True：適用於不知道會重複幾次的迴圈
# 兩個維度的清單，清單中還有清單
products = [] #清單，裝著輸入的商品
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    price = int(price)
    products.append([name, price])  
print(products)

# 印出所有商品紀錄 （第二步驟）
for p in products:
    print(p[0], '的價格是', p[1])

# 寫入檔案（第三步驟）
# 'abc' + 'abc' = 'abcabc'
# 'abc' * 3 = 'abcabcabc'
# open 打開檔案
# 'w' 寫入，先打開才能寫入
# enconding 編碼，寫入檔案和讀取檔案，都有編碼的問題
with open('products.csv', 'w', encoding = 'utf-8') as f:  #電腦原本有無'products.txt/csv'都無關係
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ', ' + str(p[1]) + '\n')
        # 字串 + 字串  
		#str() 把int(price)轉換成字串  ；\n 換行