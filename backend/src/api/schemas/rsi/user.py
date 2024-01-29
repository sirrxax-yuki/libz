from pydantic import BaseModel, Field

class RSILicense(BaseModel):
    licenseId: str = Field('', description="RSI license ID.")
    serviceClass: str = Field('', description="RSI service name.")
    volumeType: str = Field('', description="RSI license volume type.")
    beginningAt: str | None = Field(None, description="License beginning date.")
    endingAt: str | None = Field(None, description="License ending date.")
    contractId: str | None = Field(None, description="RSI contract ID.")
    contractSystemId: str | None = Field(None, description="RSI contract system ID.")
    contractSystemExtension: dict = Field({}, description="Extension.")

class RSIPermittedService(BaseModel):
    serviceClass: str = Field('', description="RSI service name.")
    permittedLicenses: list[RSILicense] = Field([])
    registeredClients: list[dict] | None = Field(None, description="Client list for RSI service.")

class RSIUserExtensionInfo(BaseModel):
    tenantId: str = Field('', description="User's tenant ID.")
    userId: str = Field('', description="User's ID.")
    status: str = Field('', description="User's status. (ex. active)")
    description: str | None = Field(None, description="User info.")
    roles: list[str] = Field([], description="User's role list.")
    permittedServices: list[RSIPermittedService] = Field([], description="Service list allowed for this user.")

class RSIUser(BaseModel):
    sub: str = Field('', description="RSI user object UUID.")
    name: str = Field('', description="User's name. (family name + given name)")
    family_name: str = Field('', description="User's family name.")
    given_name: str = Field('', description="User's given name.")
    zoneinfo: str = Field('', description="Timezone. (ex. Asia/Tokyo)")
    locale: str | None = Field(None, description="Locale.")
    ext: RSIUserExtensionInfo = Field(RSIUserExtensionInfo(), description="RSI User extension info.")
    updated_at: int = Field(0, description="Timestamp for latest updates.")
