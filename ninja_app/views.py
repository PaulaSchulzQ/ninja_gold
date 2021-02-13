from django.shortcuts import render, redirect
import random
from datetime import datetime


def index(request):
    if 'oro' not in request.session:
        request.session['oro'] = 0
        request.session['actividad'] = []

    print(f' tu_oro = {request.session["oro"]}')
    return render(request, 'index.html')


def process_money(request):
    if request.method == "POST":

        timestamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")

        if request.POST['lugar'] == "granja":
            print('Haz ido a la granja')
            request.session['oro'] += random.randint(10, 20)
            act = f"<li class='estado_ganar'> Obtuviste {request.session['oro']} de oro en la granja({timestamp}) </li>"

        if request.POST['lugar'] == "cueva":
            print('Haz ido a la cueva')
            request.session['oro'] += random.randint(5, 10)
            act = f"<li class='estado_ganar'> Obtuviste {request.session['oro']} de oro en la cueva ({timestamp}) </li>"

        if request.POST['lugar'] == "casa":
            print('Haz ido a tu casa')
            request.session['oro'] += random.randint(2, 5)
            act = f"<li class='estado_ganar'> Obtuviste {request.session['oro']} de oro en tu casa ({timestamp}) </li>"

        if request.POST['lugar'] == "casino":
            print('Cuidado fuiste al casino')
            ganar_perder = random.randint(0, 1)
            print('', ganar_perder)
            if ganar_perder == 0:
                mi_oro = random.randint(0, 50)
                request.session['oro'] -= mi_oro
                act = f"<li class='estado_perder'> Que mala suerte, haz perdido -{mi_oro} de oro ({timestamp}) </li>"
            elif ganar_perder == 1:
                mi_oro = random.randint(0, 50)
                request.session['oro'] += mi_oro
                act = f"<li class='estado_ganar'> Que buena suerte, haz ganado {mi_oro} de oro ({timestamp}) </li>"

        request.session['actividad'].append(act)

    return redirect('/')


def limpiar_session(request):
    print('\n *********** \n')
    request.session.clear()
    if 'oro' in request.session:
        del request.session['oro']

    return redirect('/')
