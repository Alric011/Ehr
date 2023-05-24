from . import db
from flask_login import UserMixin
import datetime

class Note(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000)) 
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class To_Dos(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

class User(db.Model, UserMixin): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(150), nullable=False)
    bloodgrp = db.Column(db.String(150), nullable=False)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    heart_attack = db.Column(db.Integer)
    notes = db.relationship('Note')
    todos = db.relationship('To_Dos')
    diabetes = db.relationship('Diabetes')
    # details = db.relationship('Details')

# class Details(db.Model): # type: ignore
#     id = db.Column(db.Integer, primary_key=True)
#     age = db.Column(db.Integer)
#     gender = db.Column(db.String(150), nullable=False)
#     bloodgrp = db.Column(db.String(150), nullable=False)
#     weight = db.Column(db.Integer)
#     height = db.Column(db.Integer)
#     heart_attack = db.Column(db.Integer)
#     date_created = db.Column(db.DateTime, default = datetime.datetime.now)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Diabetes(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    pregnancies = db.Column(db.Integer)
    glucose = db.Column(db.Integer)
    bloodpressure = db.Column(db.Integer)
    skinthickness = db.Column(db.Integer)
    insulin = db.Column(db.Integer)
    BMI = db.Column(db.Integer)
    DiabetesPedigreeFunction = db.Column(db.Integer)
    age = db.Column(db.Integer)
    pred_diabetes = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default = datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Heart(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    cp = db.Column(db.Integer)
    rbp = db.Column(db.Integer)
    chol = db.Column(db.Integer)
    fbs = db.Column(db.Integer)
    recg = db.Column(db.Integer)
    mhra = db.Column(db.Integer)
    exia = db.Column(db.Integer)
    oldpeak = db.Column(db.Integer)
    slope = db.Column(db.Integer)
    vcf = db.Column(db.Integer)
    thal = db.Column(db.Integer)
    pred_heart = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default = datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Park(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    mdvp_fo = db.Column(db.Integer)
    mdvp_fhi = db.Column(db.Integer)
    mdvp_flo = db.Column(db.Integer)
    mdvp_jitter = db.Column(db.Integer)
    mdvp_jitter_abs = db.Column(db.Integer)
    mdvp_rap = db.Column(db.Integer)
    mdvp_ppq = db.Column(db.Integer)
    jitter_ddp = db.Column(db.Integer)
    mdvp_shimmer = db.Column(db.Integer)
    mdvp_shimmer_db = db.Column(db.Integer)
    mdvp_shimmer_apq3 = db.Column(db.Integer)
    mdvp_shimmer_apq5 = db.Column(db.Integer)
    mdvp_apq = db.Column(db.Integer)
    shimmer_dda = db.Column(db.Integer)
    nhr = db.Column(db.Integer)
    hnr = db.Column(db.Integer)
    rpde = db.Column(db.Integer)
    dfa = db.Column(db.Integer)
    spread1 = db.Column(db.Integer)
    spread2 = db.Column(db.Integer)
    d2 = db.Column(db.Integer)
    ppe = db.Column(db.Integer)
    pred_park = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default = datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))