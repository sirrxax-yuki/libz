export default interface RSILicense {
    licenseId: string,
    serviceClass: string,
    volumeType: string,
    beginningAt?: string,
    endingAt?: string,
    contractId?: string
    contractSystemId?: string,
    contractSystemExtension?: { [key: string]: any },
}
