from pydantic import BaseModel


class BaseAPISchemaModel(BaseModel):
    class Config:
        from_attributes = True