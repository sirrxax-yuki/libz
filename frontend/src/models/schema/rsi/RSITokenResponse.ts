export default interface RSITokenResponse {
    token_type: string,
    access_token: string,
    refresh_token: string,
    id_token: string,
    expires_in: number,
}
