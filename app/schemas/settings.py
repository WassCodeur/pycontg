from pydantic import BaseModel, EmailStr, Field


class Settings(BaseModel):
    env: str = Field(..., title="Environment",
                     description="The environment in which the application is running (e.g., dev, prod)")
    name: str = Field(..., title="Application Name",
                      description="The name of the application")
    version: str = Field(..., title="Application Version",
                         description="The version of the application")
    algorithm: str = Field(..., title="JWT Algorithm",
                           description="The algorithm used for encoding JWT tokens")
    secret_key: str = Field(..., title="JWT Secret Key",
                            description="The secret key used for encoding and decoding JWT tokens")
    access_token_expire_minutes: int = Field(..., title="Access Token Expiration",
                                             description="The number of minutes until the access token expires")
    supabase_url: str = Field(..., title="Supabase URL",
                              description="The URL of the Supabase instance")
    supabase_key: str = Field(..., title="Supabase Key",
                              description="The API key for accessing the Supabase instance")
    smtp_server: str = Field(..., title="SMTP Server",
                             description="The SMTP server address for sending emails")
    smtp_port: int = Field(..., title="SMTP Port",
                           description="The port number for the SMTP server")
    smtp_user: str = Field(..., title="SMTP User",
                           description="The username for authenticating with the SMTP server")
    smtp_pass: str = Field(..., title="SMTP Password",
                           description="The password for authenticating with the SMTP server")
