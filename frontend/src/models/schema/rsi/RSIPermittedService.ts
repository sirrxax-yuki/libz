import RSILicense from "./RSILicense";

export default interface RSIPermittedService {
    serviceClass: string,
    permittedLicenses: RSILicense[],
    registeredClients?: { [ key: string ]: any }[],
}
