# 密碼重試程式
# 先在程式碼中設定好密碼，並讓使用者『最多輸入三次密碼』
# 不對的話，就印出"密碼錯誤！還有＿次機會"
password = "a123456"
login_time = 1 #嘗試次數
while login_time <= 3:
	question = input("請輸入密碼： （最多嘗試三次）")
	if question == password:
		input("登入成功")
		break
	elif question != password and login_time <= 2:
		print("密碼錯誤，剩餘" , 3 - login_time , "次機會")
	elif question != password and login_time == 3:
		print("密碼錯誤，將結束程式")
	login_time = login_time + 1