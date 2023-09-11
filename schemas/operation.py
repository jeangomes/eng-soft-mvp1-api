from pydantic import BaseModel
from typing import List
from model.operation import Operation
from datetime import datetime


class OperationSchema(BaseModel):
    """ Define como uma nova operação a ser inserida deve ser representada
    """
    operation_type: str = "Compra"
    code: str = "ITSA4"
    quantity: int = 56
    price: float = 12.25
    operation_date: str = "2019-08-30"


class ListOperationsSchema(BaseModel):
    """ Define como uma listagem de operações será retornada.
    """
    operations: List[OperationSchema]


def show_operations(operations: List[Operation]):
    """ Retorna uma representação da operação seguindo o schema definido em
        OperationViewSchema.
    """
    result = []
    for operation in operations:
        result.append({
            "id": operation.id,
            "operation_type": operation.operation_type,
            "code": operation.code,
            "quantity": operation.quantity,
            "price": operation.price,
            "operation_date": datetime.strptime(str(operation.operation_date), "%Y-%m-%d").strftime("%d/%m/%Y"),
            "operation_amount": operation.operation_amount,
        })

    return {"operations": result}


class OperationViewSchema(BaseModel):
    """ Define como uma operação será retornada: operation.
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
        "operation_date": str(operation.operation_date),
        "operation_amount": operation.operation_amount,
        "created_at": operation.created_at
    }


class OperationBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca.
    """
    operation_id: int = 1


class OperationDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de exclusão.
    """
    message: str
    nome: str
