from pydantic import BaseModel
from typing import Optional, List
from model.operation import Operation


class OperationSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    operation_type: str = "Compra"
    code: str = "ITSA4"
    quantity: int = 50
    price: float = 12.50
    operation_date: str = "2023-08-11"


class OperationViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    operation_type: str = "Compra"
    code: str = "ITSA4"
    quantity: int = 50
    price: float = 12.50
    operation_date: str = "2023-08-11"


def show_operation(operation: Operation):
    """ Retorna uma representação da operação seguindo o schema definido em
        OperationViewSchema.
    """
    return {
        "operation_type": operation.operation_type,
        "code": operation.code,
        "quantity": operation.quantity,
        "price": operation.price,
        "operation_date": operation.operation_date,
        "operation_amount": operation.operation_amount,
        "created_at": operation.created_at
    }
