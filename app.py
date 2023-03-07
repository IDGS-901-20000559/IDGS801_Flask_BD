from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms
from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()

@app.route('/', methods = ['GET', 'POST'])
def index():
    create_forms = forms.UserForm(request.form)
    if request.method == 'POST':
        alumn = Alumnos(nombre = create_forms.nombre.data,
                        apellidos = create_forms.apellidos.data,
                        email = create_forms.email.data)
        
        #Con esto insertamos
        db.session.add(alumn)
        #Con la sig. linea se mantienen los cambios
        db.session.commit()

    return render_template('index.html', form = create_forms)

@app.route("/ABCompleto", methods = ['GET', 'POST'])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    # Para poder realizar una consulta usando SQLAlchemy
    alumnos = Alumnos.query.all()
    return render_template('ABCompleto.html', 
                           form = create_form, 
                           alumnos = alumnos)

@app.route("/modificar", methods = ['GET', 'POST'])
def modificar():
    create_forms = forms.UserForm(request.form)
    
    # Se pretende que muestre una pantalla con los datos del registro
    # Con el fin de que se pueda modificar
    if request.method == 'GET':
        # Obtiene el valor por medio de los parametros en el URL
        id = request.args.get('id')
        # SELECT * FROM ALUMNOS WHERE id == id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_forms.nombre.data = alum1.nombre
        create_forms.apellidos.data = alum1.apellidos
        create_forms.email.data = alum1.email

    if request.method == 'POST':
         id = request.args.get('id')
        # SELECT * FROM ALUMNOS WHERE id == id
         alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
         alum.nombre = create_forms.nombre.data
         alum.apellidos = create_forms.apellidos.data
         alum.email = create_forms.email.data

         db.session.add(alum)
         db.session.commit()


if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)