from database.connection import engine
from models.base import Base

def create_db():
    
    print("Criando o banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Banco de dados criado com sucesso!")

if __name__ == "__main__":
    create_db()