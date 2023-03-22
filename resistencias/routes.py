from db import get_connection
from flask import Blueprint, Flask, redirect, jsonify, render_template
from flask import request
from flask import url_for
import forms
from config import DevelopmentConfig

from flask import Flask, render_template, request, redirect, make_response, flash
from forms import UserForm 
import forms

resistencias = Blueprint('resistencias',__name__)

@resistencias.route("/resistencias", methods=['GET', 'POST'])
def calResistencia():
    resistencia_form = forms.ResistenciaForm(request.form)

    if request.method == 'POST':
        colors = obtenerColores()
        
        codigo_colores = {
          colors[0]: 0,
          colors[1]: 1,
          colors[2]: 2,
          colors[3]: 3,
          colors[4]: 4,
          colors[5]: 5,
          colors[6]: 6,
          colors[7]: 7,
          colors[8]: 8,
          colors[9]: 9,
          colors[10]: 0.05,
          colors[11]: 0.1
        }

        color1 = resistencia_form.bandaUno.data
        color2 = resistencia_form.bandaDos.data
        color3 = resistencia_form.bandaTres.data
        color4 = request.form.get('tolerance')

        bandaUno = codigo_colores[color1]
        bandaDos = codigo_colores[color2]
        bandaTres = codigo_colores[color3]
        tolerancia = codigo_colores[color4]

        valorNominal = (bandaUno * 10 + bandaDos) * 10 ** bandaTres

        minimo = 0
        maximo = 0
        if tolerancia == 0.05:
            maximo = valorNominal + valorNominal*(0.05)
            minimo = valorNominal - valorNominal*(0.05)
        elif tolerancia == 0.1:
            maximo = valorNominal + valorNominal*(0.1)
            minimo = valorNominal - valorNominal*(0.1)

        return render_template('resistencias.html', form = resistencia_form, color1 = color1, color2 = color2, color3 = color3, color4 = color4, 
                               valorNominal = valorNominal, minimo =  minimo, maximo = maximo)
    
    return render_template('resistencias.html', form = resistencia_form)

def obtenerColores():
    with open('colores.txt', 'r') as f:
     lista = [linea.strip() for linea in f.readlines()]
     return lista
