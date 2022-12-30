from typing import Generic, Optional, Type, TypeVar

from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    async def get_by_name(self, name: str) -> Optional[ModelType]:
        result = await self.model.find_one(self.model.name == name)
        return result
