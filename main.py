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
user = auth.sign_in_with_email_and_password("jesiel.bv@gmail.com", 'teste123')

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
	print(f'Projeto criado com sucesso✓')
	
	
	
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
	
	