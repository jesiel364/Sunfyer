import pyrebase
import json

config = {
  "apiKey": "AIzaSyA2AhM0VBM2gZHgY0HPFFQUfdVYJS9usTI",
  "authDomain": "primeiro-projeto-6d3f8.firebaseapp.com",
  "databaseURL": "https://primeiro-projeto-6d3f8-default-rtdb.firebaseio.com",
  "projectId": "primeiro-projeto-6d3f8",
  "storageBucket": "primeiro-projeto-6d3f8.appspot.com",
  "messagingSenderId": "1010182689466",
  "appId": "1:1010182689466:web:dc21fcf1cae43e395e2883",
  "measurementId": "G-L4S33QDE2S"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
user = auth.sign_in_with_email_and_password("jesiel364@gmail.com", '12345678')

db = firebase.database()

print(' Bem vindo ao Sunfyer')

menu = input('1 - Adicionar Projeto \n2 - Logar Usuário \n3 - Criar Conta \n4 - Ver Projetos \n')

DAW_LIST = '1 - FL Studio \n2 - Reaper \n3 - Cubase \n4 - Ableton Live'

if menu == '1':
	print('\nEscolha sua DAW')
	
	print(DAW_LIST)
	project_name = input('\nAdd Project: ')
	
	if project_name == '1':
		daw = 'FL Studio'
	elif project_name == '2':
		daw = 'Reaper'
	elif project_name == '3':
		daw = 'Cubase'
	elif project_name == '4':
		daw = 'Ableton Live'
	
	nome = input('Nome do projeto: ')
		
	data = {
		'titulo': f'{nome}',
		'etapa': 'Produção'
	}
	
	
	db.child('Sunfyer - DAW Projects').child('Projects').child(daw).push(data, user['idToken'])
	print(f'Projeto criado com sucesso ✓')

elif menu == '2':
	print('Fazer Login\n')
	user_email = input('Email: ')
	user_p = input('Senha: ')
	try:
		user = auth.sign_in_with_email_and_password(user_email, user_p)
		info = auth.get_account_info(user['idToken'])
		auth.send_email_verification(user['idToken'])
		print(info)
		print('Usuário Logado ✓')
	except:
		print('Email ou senha não encontrados!')

elif menu == '3':
	print('Criar Conta\n')
	user_n = input('Nome de Usuário: ')
	user_email = input('Email: ')
	user_p = input('Senha: ')
	try:
		auth.create_user_with_email_and_password(user_email, user_p)
		print('Conta criada com sucesso ✓')
	except:
		print('Algo deu errado!')
	
	
elif menu == '4':
	print('Ver Projetos\n')
	menu_show = input(DAW_LIST)
	
	if menu_show == '1':
		daw = 'FL Studio'
		print(f'Projetos {daw}\n')
		proj = db.child('Sunfyer - DAW Projects').child('Projects').child(daw).get()
		for item in proj.each():
			print('Titulo: ' + item.val()['titulo'])
			print('Etapa: '  + item.val()['etapa'])
		
	elif menu_show == '2':
		daw = 'Reaper'
		print(f'Projetos {daw}\n')
		proj = db.child('Sunfyer - DAW Projects').child('Projects').child(daw).get()
		for item in proj.each():
			print('Titulo: ' + item.val()['titulo'])
			print('Etapa: '  + item.val()['etapa'])
	
	elif menu_show == '3':
		daw = 'Cubase'
		print(f'Projetos {daw}\n')
		proj = db.child('Sunfyer - DAW Projects').child('Projects').child(daw).get()
		for item in proj.each():
			print('Titulo: ' + item.val()['titulo'])
			print('Etapa: '  + item.val()['etapa'])
		
	elif menu_show == '4':
		daw = 'Ableton Live'
		print(f'Projetos {daw}\n')
		proj = db.child('Sunfyer - DAW Projects').child('Projects').child(daw).get()
		for item in proj.each():
			print('Titulo: ' + item.val()['titulo'])
			print('Etapa: '  + item.val()['etapa'])
	
	