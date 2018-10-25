import pyttsx3
en=pyttsx3.init()
en.setProperty('voice',b'brazil')
en.say("Bom dia Turma")
en.say("Bem Vindos ao Instituto Federal de Educação - IFSUL campus Sapiranga")
en.say("Quarto ano do curso técnico em Informática")
en.runAndWait()