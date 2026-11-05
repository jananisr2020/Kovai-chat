from pydantic import BaseModel, ConfigDict, Field

class MenuItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    category: str
    description: str
    price: float
    is_available: bool

class RestaurantOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    area: str
    description: str
    is_open: bool

class OrderCreate(BaseModel):
    customer_name: str = Field(min_length=2, max_length=160)
    customer_phone: str = Field(min_length=10, max_length=20)
    delivery_address: str = Field(min_length=8)
    total_amount: float = Field(gt=0)
