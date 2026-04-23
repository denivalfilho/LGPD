from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, DateTime, insert, text
from datetime import datetime

import time
from functools import wraps
def medir_tempo(func):
    """Decorator que mede o tempo de execução de uma função."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()  # tempo inicial (mais preciso que time.time)
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()     # tempo final
        duracao = fim - inicio
        print(f"⏱ Função '{func.__name__}' executada em {duracao:.6f} segundos.")
        return resultado
    return wrapper

engine = create_engine("postgresql+psycopg2://alunos:AlunoFatec@200.19.224.150:5432/atividade2", echo=False)
metadata = MetaData()

usuarios = Table(
    'usuarios', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50), nullable=False, index=True),
    Column('cpf', String(14), nullable=False),
    Column('email', String(100), nullable=False, unique=True),
    Column('telefone', String(20), nullable=False),
    Column('data_nascimento', Date, nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

metadata.create_all(engine)

@medir_tempo
def LGPD(row):
    row_lista = list(row)

    nome_completo = row_lista[1]
    primeiro_nome = nome_completo.split()[0]
    resto_do_nome = nome_completo[len(primeiro_nome):]
    row_lista[1] = primeiro_nome[0] + ("*" * (len(primeiro_nome)-1)) + resto_do_nome

    cpf_original = row_lista[2]
    row_lista[2] = cpf_original[0:4] + "***.***-**"

    email = row_lista[3]
    usuario, dominio = email.split("@")
    row_lista[3] = usuario[0] + ("*" * 9) + "@" + dominio

    telefone = row_lista[4]
    row_lista[4] = telefone[-4:]

    return tuple(row_lista)

users = []
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM usuarios LIMIT 5;"))
    for row in result:
        row = LGPD(row)
        users.append(row)

for user in users:
    print(user)
