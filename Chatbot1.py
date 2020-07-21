def greeting():
  my_age = 99
  # This signifies my age and, as a game, half of my age. I discontinued the "my_age" integer being used
  half_my_age = my_age / 2
  my_name = "insert"
  greeting = "Hi! How are you? My name is "
  greeting_with_name = greeting + my_name + ". "
  ask_name_question = "What's yours?"
  print(greeting_with_name + ask_name_question)

greeting()
