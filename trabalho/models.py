from trabalho import db
from datetime import datetime


class Contato(db.Model):
    id = db.column(db.Integer, primary_key=True)
    data_envio = db.column(db.DateTime, default = datetime.utcnow())
    nome = db.column(db.string, nullable=True)
    email = db.column(db.string, nullable=True)
    assunto = db.column(db.string, nullable=True)
    mensagem = db.column(db.string, nullable=True)
