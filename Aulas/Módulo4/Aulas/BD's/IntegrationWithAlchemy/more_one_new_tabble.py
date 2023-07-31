from sqlalchemy.orm import declarative_base,relationship,Session
from sqlalchemy import Column,Integer,String,ForeignKey,create_engine,inspect,select,func


Base = declarative_base()

class User(Base):
    __tablename__ = "Usuario"

    id = Column(
        Integer,
        primary_key = True
    )
    name = Column(
        String
    )
    full_name = Column(
        String
    )
    address = relationship(
        "Address",
        back_populates = "user",
        cascade = "all,delete-orphan"
    )

    def __repr__(self):
        return(f"User(id = {self.id}), name = {self.name}, full_name = {self.full_name}")

class Address(Base):
    __tablename__ = "Endereço"

    id = Column(
        Integer,
        primary_key = True,
        autoincrement = True
    )
    email_address = Column(
        String(30),
        nullable = False
    )
    user_id = Column(
        Integer,ForeignKey("Usuario.id"), #as chaves estrangeiras referenciam os nomes das mesas e seus repectivos atributos,não as classes de declarações
        nullable = False 
    )
    user = relationship(
        "User",
        back_populates = "address",
        # cascade = "all,delete-orphan"
    )
    
    def __repr__(self):
        return(f"Address(id = {self.id}), email = {self.email_address},")
    


print(User.__tablename__)
print(Address.__tablename__)


# Conexão com banco de dados:
engine = create_engine("sqlite://") 

# Criando as classes como tabelas no BD
Base.metadata.create_all(engine)

# Criação um inspetor
insp = inspect(engine)

# Verificando a existência de uma mesa
print(insp.has_table("Endereço"))


print(insp.get_table_names)
print(insp.default_schema_name)

with Session(engine) as session:
    Breno = User(
        id = 12345,
        name = "Breno",
        full_name = "Breno Breno",
        address = [Address(email_address = "brenopositivo@hotmail.com")]
    )
    Amanda = User(
        id = 88761,
        name = "Amanda",
        full_name = "Amanda Amanda Amanda",
        address = [Address(email_address = "Amandalinda21@gmail.com"),Address(email_address = "AmandaAmandaAmanda@mail.com ")]
    )
    Patrick = User(
        id = 58747,
        name = "Patrick",
        full_name = "Patrick Estrela dos santos",
        address = [Address(email_address = "bobspongefriend@gmail.com"),Address(email_address = "patrickstar@mail.com ")]
    )

# Enviando para o Banco de Dados
session.add_all([Breno,Amanda,Patrick])
session.commit()

search_users = select(User).where(User.name.in_(["Breno","Patrick"])) # parametro para consultas

# for x in session.scalars(search_users): # laço de consultas
#     print(x)

# serach_address = select(Address).where(Address.user_id.in_([58747]))

# for x in session.scalars(serach_address):
#     print(x)

# order_stmt = (select(User).order_by(User.full_name.desc())) # O order_by por padrão é ascedente

# for result in session.scalars(order_stmt):
#     print(f"reesult = {result}")

# search_with_join = select(User.full_name,Address.email_address).join_from(Address,User)

# for x in session.scalars(search_with_join):
#     print(f'full_name = {x}',end = "\n")
    

# conection = engine.connect()
# results = conection.execute(search_with_join).fetchall() # executando statement a partir da connection

# for result in results:
#     print(result)

order = (select(User).order_by(User.full_name.desc()))

# for result in session.scalars(order):
#     print(result,end = "\n")

smtm_join = select(User.full_name,Address.email_address).join_from(User,Address)

for x in(session.scalars(smtm_join)),session.scalars(smtm_join):
    print(x,"\n")

conection = engine.connect()

results = conection.execute(smtm_join).fetchall() # pra retornar tudo com o join é desse jeito!

for result in results:
    print(result,"\n")


contagem = (select(func.count('*')).select_from(User))

for c in session.scalars(contagem):
    print(c,"\n")