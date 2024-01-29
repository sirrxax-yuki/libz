export default interface RSIAuthRequest {
    client_id: string,
    redirect_uri: string,
    response_type: string,
    response_mode: string,
    scope: string,
    login_page: string,
    code_challenge: string,
    code_challenge_method: string,
}
