import keyboard
import time


key = input('Кнопка на которую вы хотите начать спам: ')
request = input('Введите текст который вы хотите что бы писался при спаме: ')
peremennaya = input('Кол-во сообщений отправлять: ')
delay = input('скорость отправки сообщений:')

print(f'Нажмите {key}')

def click():
	for i in range(int(peremennaya)):
		keyboard.write(request)
		time.sleep(float(delay))
		keyboard.send('Enter')
def loop():
	while True:
		if keyboard.is_pressed(key):
			click()
loop()