export default interface RSITokenRequest {
    grant_type: string,
    client_id: string,
    redirect_uri: string,
    code: string,
    code_verifier: string,
}
