import pyautogui, pyperclip, random, time
messenger_ = input("Nội dung: ").split(" || ")
times_ = int(input("Số lần=>>"))
delay_ = float(input("Delay=>>"))
print("Ready!")
for i in range(3,0,-1):
	print(i,flush='True')
	time.sleep(1)
print("Spam!")
for i in range(times_):
	pyperclip.copy(random.choice(messenger_))
	pyautogui.hotkey("ctrl","v")
	pyautogui.press("enter")
	time.sleep(delay_)
