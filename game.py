preguntas =[

]
Respuestas =[

]#Respuestas correctas
def quiz():
    puntaje = 0
    for i in range(len(preguntas)):
        print("\n" + preguntas[i])
        Respuesta_user = input("Digite la respuesta que considera correcta 'a','b','c':").lower()
        if Respuesta_user == Respuestas[i]:
            print ("¡Eres fantastico!")
            puntaje += 1
        else:
            print (f"jajajajaj sigue intentando, la respuesta correcta es"+ Respuestas[i])
    print (f"Tu puntaje total es: {puntaje}/{len(preguntas)}")

quiz()