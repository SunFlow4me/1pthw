from sys import argv

script, user_name = argv
prompt = '> '

print(f"приветствую {user_name}, это - {script}.")
print("Задам пару вопросов.")
print(f"итак {user_name}, скажи своё настоящее имя")
name = input(prompt)

print("как твоё настроение?")
mood = input(prompt)

print("и последнее, что скажешь президенту при встрече?")
answer = input(prompt)
print(f"""
твоё настоящее имя {name}
твоё настроение {mood}
и ты скажешь '{answer}', отличненько
""")
