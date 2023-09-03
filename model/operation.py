from sqlalchemy import Column, String, Integer, Date, Float
# from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class Operation(Base):
    __tablename__ = 'finance_operation'

    id = Column("pk_produto", Integer, primary_key=True)
    operation_type = Column(String(20))
    code = Column(String(10))
    quantity = Column(Integer)
    price = Column(Float)
    operation_date = Column(Date, default=datetime.now())
    operation_amount = Column(Float)

    def __init__(self, operation_type: str, code: str, quantity: int, price: float,
                 operation_date: Union[Date, None] = None):
        """
        Cria um Produto

        Arguments:
            operation_type: nome do produto
            code: nome do produto
            quantity: quantidade que se espera comprar daquele produto
            price: valor esperado para o produto
            operation_date: data de quando o produto foi inserido à base
        """
        self.operation_type = operation_type
        self.code = code
        self.quantity = quantity
        self.price = price
        self.operation_date = self.format_date(operation_date)

    def format_date(self, my_date):
        operation_date_object = datetime.strptime(my_date, "%Y-%m-%d")
        return operation_date_object.date()
