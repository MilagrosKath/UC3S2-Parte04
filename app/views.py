from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layout = """
    <h3>
        <ul>
            <li>
                <a href="/inicio">Inicio</a>
            </li>
            <li>
                <a href="/primos">Numeros primos entre [a] y [b]</a>
            </li>
            <l1>
                <a href="/examen">Examen</a>
            </li>
        </ul>
    </h3>
    <hr>
"""
def inicio(request):
    mensaje = """
        <h1>Lenguaje de programación III</h1>
        <h2>Integrantes:</h2>
        <h2>
            <ul>
                <li>Barzola Navarro, Danee</li>
                <li>Gonzales Castillo, Daniel</li>
                <li>Soto Obregón, Milagros Katherine
                 </li>
            </ul>
        </h2>
    """
    return HttpResponse(layout+mensaje)

def primos(request, a=0, b=100):
    if a > b:
        temp = b
        b = a
        a = temp
    a1 = a
    b1 = b
    mensaje = f"""
        <h2>Mostrando numeros primos desde {a} hasta {b}</h2>
        <ul>
    """
    while a <= b:
        contador = 1
        x = 0
        while(contador <= a):
            if a % contador == 0:
                x = x+1
            contador = contador + 1
        if x == 2:
            mensaje += f"<li>{a}</li>"
        a = a + 1
    mensaje += "</ul>"
    return HttpResponse(layout+mensaje)

def examen(request):
    mensaje2="""
        <h1>GitHub del Proyecto</h1>
        <h2>
            <ul>
                <li>Soto Obregón, Milagros Katherine
                <br>https://github.com/MilagrosKath/UC3S2_Parte01.git </li>
                <li>Barzola Navarro, Danee
                <br>https://github.com/DaneeJhajaira2002/UC3S2-Parte02.git
                </li>
                <li>Gonzales Castillo, Daniel
                <br>https://github.com/DanXanDer/UC3S2-Parte03.git</li>
                <li>Soto Obregón, Milagros Katherine
                <br>https://github.com/MilagrosKath/UC3S2-Parte04.git</li>
            </ul>
        </h2>
    """
    return HttpResponse(layout+mensaje2)