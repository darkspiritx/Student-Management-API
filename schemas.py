from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=1, le=100)
    course: str = Field(min_length=2, max_length=50)

class StudentResponse(BaseModel):

    model_config = {
        "from_attributes": True
    }

    id: int
    name: str
    age: int
    course: str

class StudentUpdate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=1, le=100)
    course: str = Field(min_length=2, max_length=50)