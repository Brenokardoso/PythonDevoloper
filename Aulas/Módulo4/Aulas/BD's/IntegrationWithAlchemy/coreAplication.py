from sqlalchemy import Column,Integer,String,create_engine,select,MetaData,Table,ForeignKey 
from sqlalchemy.orm import declarative_base,relationship

engine = create_engine("sqlite:///:memory")

metadata_obj = MetaData(schema = "teste")
user = Table(
    'user',
    metadata_obj,
    Column(
        "user_id",
        Integer,
        primary_key = True,
    ),
    Column(
        "address",
        String(60),
    ),
    Column(
        "nickname",
        String(40),
        nullable = False
    ),
    Column(
        "nome",
        String(40),
        nullable = False
    )
)

user_prefs = Table(
    "user_prefs",
    metadata_obj,
    Column(
        "pref_id",
        Integer,
        primary_key = True
    ),
    Column(
        "user_id",
        Integer,
        ForeignKey("user.user_id"),
    ),
    Column(
        "pref_name",
        String(40),
        nullable = False
    ),
    Column(
        "pref_valor",
        String(50), 
    )
)

for table in metadata_obj.sorted_tables:
    print(table )