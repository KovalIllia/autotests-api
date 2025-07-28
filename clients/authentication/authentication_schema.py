from pydantic import BaseModel,Field

#Added suffix Schema instead of Dict
class TokenSchema(BaseModel):#We inherit from BaseModel instead of TypedDict
    """Added structure with authentication tokens"""
    token_type: str=Field(alias="tokenType")
    access_token: str=Field(alias="accessToken")
    refresh_token: str=Field(alias="refreshToken")

#Added suffix Schema instead of Dict
class LoginRequestSchema(BaseModel):
    """Description of the authentication request structure."""
    email: str
    password:str

#Added suffix Schema instead of Dict
class LoginResponceSchema(BaseModel):
    """Description of the structure of the authentication response"""
    token:TokenSchema


#Added suffix Schema instead of Dict
class RefreshRequestSchema(BaseModel):
    """Description of the structure of the request for updating the token."""
    refresh_token: str=Field(alias="refreshT oken") #in general Python named like snake_case, buy this camelCase
