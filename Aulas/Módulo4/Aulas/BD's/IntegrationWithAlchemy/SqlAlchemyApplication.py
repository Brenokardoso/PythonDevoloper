from sqlalchemy import Column,Integer,String,inspect,engine,ForeignKey,create_engine
from sqlalchemy.orm import declarative_base,relationship,Session




def mostra_dados(obj):
    print(f"Id = {obj.id},Nome = {obj.name},Nome Completo = {obj.full_name},Endereço = {obj.address}")
    pass


# Declarando o parâmetro de onde as classes herdarão:
Base = declarative_base()

# Declaração das tabela User:
class User(Base):
    __tablename__ = "Usuario"

    # Atributos da tabela User

    id = Column(Integer,primary_key = True)
    name = Column(String)
    full_name = Column(String)
    address = relationship("Address",back_populates = "user",cascade = "all,delete-orphan",uselist = False)
    def __repr__(self):
        return f"User(Id = {self.id}, name = {self.name}, full_name = {self.full_name})"

# Declaração da tabela Address:
class Address(Base):
    __tablename__ = "Endereço"

    # Atributos de Address
    id = Column(Integer,primary_key = True)
    email_address = Column(String,unique = True)    
    user_id = Column(Integer, ForeignKey("Usuario.id"), nullable=False)
    user = relationship("User",back_populates = "address")
    def __repr__(self):
        return f"Address(Id = {self.id} , email_address = {self.email_address} , user_id = {self.user_id},user = {self.user})"

# conexão com o banco de dados:
engine = create_engine("sqlite://")


# Criação das tabelas no banco de dados:
Base.metadata.create_all(engine)

# criando uma sessão para interagir com o banco de dados
with Session(engine) as session:
    breno = User(
        id = 123456789,
        name = "Breno",
        full_name = "Breno Cardoso de Castro Guimarães",
        address = Address(email_address = "brenopositivo@hotmail.com")
    )

mostra_dados(breno)
