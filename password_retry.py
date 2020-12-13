password = "a123456"
x = 3
while 0<x<=3 : #可以改成x>0，反正起始是3
    x = x - 1 #conter先扣，反正後面一定會跑。
    login = input("請輸入密碼:")
    if password != login:
        print("密碼錯誤")
        if x > 0:
            print("您還可以嘗試", x ,"次機會")
        elif x == 0:
            print("登入失敗")
            break
    else: #elif改成else，就可以不用寫條件
        print("登入成功")
        break


#檢討：conter的想法沒錯，只是login的做法需要整合到迴圈，不然會只詢問一次。
#檢討二：登入失敗的迴圈要額外放，不然conter到0的時候不會跳到第二個迴圈，會在第一個迴圈就結束掉。
#檢討三：忘記字串連接的寫法。
#檢討四：else跟elif差別在要不要寫條件，如果只有兩種情況用else比較好
#檢討五：密碼可嘗試機會變成0次的時候，conter(有用到x的部分)要確認好