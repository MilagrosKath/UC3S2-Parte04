from django.shortcuts import render, HttpResponse

# Create your views here.
layout = """
    <h3>
        <ul>
            <li>
                <a href="inicio/">Inicio</a>
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
                <li>Soto Obregón, Milagros Katherine</li>
            </ul>
        </h2>
    """
    return HttpResponse(layout+mensaje)

