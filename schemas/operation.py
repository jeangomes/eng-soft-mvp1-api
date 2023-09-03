from pydantic import BaseModel
from typing import Optional, List
from model.operation import Operation


class OperationSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    operation_type: str = "Compra"
    code: str = "ITSA4"
    quantity: int = 56
    price: float = 12.25
    operation_date: str = "2019-08-30"


class OperationViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    operation_type: str = "Compra"
    code: str = "ITSA4"
    quantity: int = 56
    price: float = 12.25
    operation_date: str = "2019-08-30"


def show_operation(operation: Operation):
    """ Retorna uma representação da operação seguindo o schema definido em
        OperationViewSchema.
    """
    return {
        "id": operation.id,
        "operation_type": operation.operation_type,
        "code": operation.code,
        "quantity": operation.quantity,
        "price": operation.price,
        "operation_date": operation.operation_date,
        "operation_amount": operation.operation_amount,
        "created_at": operation.created_at
    }
