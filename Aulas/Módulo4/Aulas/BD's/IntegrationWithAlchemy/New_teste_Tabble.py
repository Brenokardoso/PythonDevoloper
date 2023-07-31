from sqlalchemy import Column,String,Integer,create_engine,inspect,ForeignKey
from sqlalchemy.orm import declarative_base,Session,relationship

# Declaração de onde as classes irão herdar alguns comportamentos
Base = declarative_base()

class Produto(Base):
    __tablename__ = "Produtos"
    id = Column(
        Integer,
        primary_key = True,
        nullable = False
    )
    nome = Column(
        String(40),
        nullable = False
    ) 
    marca = Column(
        String(30)
    )
    cor = Column(
        String(30)
    )
    quantidade_loja = Column(
        Integer
    )
    estoque = relationship("Estoque",back_populates = "nmr_estoque",cascade ="all,delete-orphan",uselist =  False)


class Estoque(Base):
    __tablename__ = "Estoques"
    id = Column(
        Integer,
        primary_key = True
    )
    total_estoque = Column(
        Integer,
        nullable = False
    )
    qnt_estoque = Column(
        Integer,
        ForeignKey("Produtos.quantidade_loja"),
        nullable = True
    )
    nmr_estoque = relationship("Produto",back_populates ="quantidade")    

# Conexão com o banco de dados:
engine = create_engine("sqlite://")

#Criação das tabelas no banco de dados:
Base.metadata.create_all(engine)

with Session(engine) as session:
    Xampu = Produto(
        id = 245786,
        nome = "Xampu",
        marca = "Lorial Paris",
        cor = "Preto",
        quantidade_loja = 10,
        stock = Estoque(total_estoque = 30)

    )


