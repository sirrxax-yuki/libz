import RSIPermittedService from "./RSIPermittedService";

export default interface RSIUserResponse {
    sub: string,
    name: string,
    family_name: string,
    given_name: string,
    zoneinfo: string,
    locale?: string,
    ext: {
        tenantId: string,
        userId: string,
        status: string,
        description?: string,
        roles: string[],
        permittedServices: RSIPermittedService[],
    },
    updated_at: number,
}
