from trabalho import app
from flask import render_template, url_for

#rotas
@app.route("/")
def homepage():
    usuario = 'Arthur'

    context ={
        'usuario' : usuario
    }

    return render_template("homepage.html", context=context)



@app.route("/nova/") 
def novapag():
    return "next page"