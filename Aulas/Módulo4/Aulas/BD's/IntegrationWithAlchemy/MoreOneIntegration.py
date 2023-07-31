from sqlalchemy import Column,String,create_engine,inspect,select,ForeignKey,Integer,SmallInteger
from sqlalchemy.orm import declarative_base,relationship,Session


Base = declarative_base()

class Data(Base):
    __tablename__ = "Dados"

    id = Column(
        Integer,
        primary_key = True,
        autoincrement = True
    )
    nome = Column(
        String(50)
    )
    idade = Column(
        Integer
    )
    cpf = Column(
        SmallInteger
    )
    endereco = Column(
        String(50)
    )
    email = Column(
        String(50)
    )
    def __repr__(self):
        return(f"nome = {self.nome}, cpf = {self.cpf} , email = {self.email}")

class Company(Base):
    __tablename__ = "Empresa"

    id = Column(
        Integer,
        primary_key = True,
        autoincrement = True 
    )
    name = Column(
        String(40)
    )
    cnpj = Column(
        String,
        unique = True,                    
    )
    endereco = Column(
        String(40)
    )
    id_salario = Column(
        Integer,
        ForeignKey("Funcionarios.salario"),
        nullable = False,
        autoincrement = True
    )
    funcionarios = relationship(
        "Funcionarios",
        back_populates = "empresa",
    )
    def __repr__(self):
        return(f"nome = {self.name},cpnj = {self.cpnj} , endereço = {self.endereco} ")

class Employees(Base):
    __tablename__ = "Funcionarios"

    id = Column(
        Integer,
        primary_key = True,
        autoincrement = True
    )
    workpalce = Column(
        String(50)
    )
    cargo = Column(
        String(50),
        unique = True,
    )
    piso = Column(
        Integer
    )
    salario = Column(
        Integer
    )
    empresa = relationship(
        "Empresa",
        back_populates = "funcionarios"
    )
    def __repr__(self):
        return(f"cargo = {self.cargo}, piso = {self.piso} , salario = {self.salario}")


# Conexão com o BD
engine = create_engine("sqlite://")

# Criação das tabelas do BD
Base.metadata.create_all(engine)

# Atributo de inspeção
insp = inspect(engine)

print(insp.has_table("Funcionarios"))

tables = insp.get_table_names()

for name in tables :
    print(name)

with Session(engine) as session:
    Coca = Company(
        id = 14785,
        name = "CocaCola",
        cnpj = 147852,
        endereco = "A uma esquina de você",
        id_salario = 1254789
    )
 