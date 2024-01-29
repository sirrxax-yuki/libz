export default interface RSITokenIntrospectResponse {
    active: boolean,
    client_id: string,
    scope: string,
    token_type: string,
    iss: string,
    aud: string,
    sub: string,
    sub_extension: {
        user?: string,
        device?: string,
    },
    iat: number,
    exp?: number,
    nonce?: string,
}
