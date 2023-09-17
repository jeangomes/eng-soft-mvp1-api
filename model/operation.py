from sqlalchemy import Column, String, Integer, Date, DateTime, Float
from datetime import datetime

from model import Base


def format_date(my_date):
    date_object = datetime.strptime(my_date, "%Y-%m-%d")
    return date_object.date()


class Operation(Base):
    __tablename__ = 'finance_operation'

    id = Column("pk_operation", Integer, primary_key=True)
    operation_type = Column(String(20), nullable=False)
    code = Column(String(10), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    operation_date = Column(Date, nullable=False)
    operation_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    def __init__(self, operation_type: str, code: str, quantity: int, price: float,
                 operation_date: str):
        """
        Cria uma Operação Financeira

        Arguments:
            operation_type: Tipo de operação
            code: Código do ativo
            quantity: quantidade unitária do ativo
            price: cotação do ativo na data de compra
            operation_date: data de quando o ativo foi negociado
        """
        self.operation_type = operation_type
        self.code = code.upper()
        self.quantity = quantity
        self.price = price
        self.operation_date = format_date(operation_date)
