import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planetas(Base):
    __tablename__ = 'planetas'
    # Aquí se definen las columnas para la tabla planetas.
    id = Column(Integer, primary_key=True)
    planetas = Column(String(20), nullable=False)
    localización = Column(String(50), nullable=False)
    Residentes = Column(String(80), nullable=False)
    composición = Column(String(225), nullable=False)
    datos_importantes = Column(String(300), nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'
    # Aquí se definen las columnas para la tabla personajes.
    id = Column(Integer, primary_key=True)
    Personajes = Column(String(40), nullable=False)
    raza = Column(String(50), nullable=False)
    estatura = Column(String(3,2), nullable=False)
    color_ojos = Column(String(10), nullable=False)
    alias = Column(String(50), nullable=False)

class Usuarios(Base):
    __tablename__ = 'usuarios'
    # Aquí se definen las columnas para la tabla usuarios.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(20), nullable=False)
    email = Column(String(35), nullable=False)
    password = Column(String(8), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Aquí se definen las columnas para la tabla favoritos.|
    id = Column(Integer, primary_key=True)
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    planetas = relationship(Planetas)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    personajes = relationship(Personajes)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship(Usuarios)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')