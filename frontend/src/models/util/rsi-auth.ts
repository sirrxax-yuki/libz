import axios, { AxiosError } from 'axios';
import jssha from 'jssha';
import RSIAuthRequest from '@/models/schema/rsi/RSIAuthRequest';
import RSITokenRequest from '@/models/schema/rsi/RSITokenRequest';
import RSITokenResponse from '@/models/schema/rsi/RSITokenResponse';
import RSITokenIntrospectResponse from '@/models/schema/rsi/RSITokenIntrospectResponse';
import RSITokenUpdateRequest from '@/models/schema/rsi/RSITokenUpdateRequest';
import RSITokenUpdateResponse from '@/models/schema/rsi/RSITokenUpdateResponse';
import RSIUserResponse from '@/models/schema/rsi/RSIUserResponse';


export default {

    async requestToken(codeVerifier: string, code: string): Promise<RSITokenResponse> {
        const param = this.createTokenRequestParameter(codeVerifier, code);
        const response = await axios.post<RSITokenResponse>(import.meta.env.VITE_RSI_TOKEN_API_URL, param);
        return response.data;
    },

    async requestUserInfo(accessToken: string): Promise<RSIUserResponse> {
        const response = await axios.get<RSIUserResponse>(import.meta.env.VITE_RSI_USER_INFO_API_URL, {
            headers: { Authorization: `Bearer ${accessToken}` },
        });
        return response.data;
    },

    async introspectToken(token: string): Promise<boolean> {
        const param = { token: token };
        try {
            const response = await axios.post<RSITokenIntrospectResponse>(import.meta.env.VITE_RSI_TOKEN_INTROSPECT_API_URL, param);
            return response.data.active;
        }
        catch (_: any) {
            return false;
        }
    },

    async updateAccessToken(refreshToken: string): Promise<RSITokenUpdateResponse> {
        const param = this.createTokenUpdateRequestParameter(refreshToken);
        const response = await axios.post<RSITokenUpdateResponse>(import.meta.env.VITE_RSI_TOKEN_API_URL, param);
        return response.data;
    },

    async revokeAccessToken(accessToken: string): Promise<void> {
        const param = { token: accessToken };
        await axios.post(import.meta.env.VITE_RSI_REVOKE_AUTH_API_URL, param);
    },
    
    createCodeVerifier(): string {
        // Specified in RFC7636
        const source = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~';
        const length = 43;
        return Array.from(crypto.getRandomValues(new Uint8Array(length))).map((n) => source[n % source.length]).join('');
    },

    createAuthorizeURL(codeVerifier: string): string {
        const param = this.createAuthorizeQuery(codeVerifier);
        const query = Object.entries(param).map(([k, v]) => `${k}=${v}`).join('&');
        return `${import.meta.env.VITE_RSI_AUTH_API_URL}?${query}`;
    },

    createLogoutURL(codeVerifier: string): string {
        const url = this.createAuthorizeURL(codeVerifier);
        return `${import.meta.env.VITE_RSI_LOGOUT_PAGE_URL}?url=${encodeURIComponent(url)}`;
    },

    createAuthorizeQuery(codeVerifier: string): RSIAuthRequest {
        return {
            client_id: import.meta.env.VITE_RSI_CLIENT_ID,
            redirect_uri: import.meta.env.VITE_RSI_AUTH_REDIRECT_URL,
            response_type: 'code',
            response_mode: 'query',
            scope: 'offline_access openid profile',
            login_page: 'rsi_user_site_user_id',
            code_challenge: this.convertToCodeChallenge(codeVerifier),
            code_challenge_method: 'S256',
        };
    },

    createTokenRequestParameter(codeVerifier: string, code: string): RSITokenRequest {
        return {
            grant_type: 'authorization_code',
            client_id: import.meta.env.VITE_RSI_CLIENT_ID,
            redirect_uri: import.meta.env.VITE_RSI_AUTH_REDIRECT_URL,
            code: code,
            code_verifier: codeVerifier,
        };
    },

    createTokenUpdateRequestParameter(refreshToken: string): RSITokenUpdateRequest {
        return {
            grant_type: 'refresh_token',
            client_id: import.meta.env.VITE_RSI_CLIENT_ID,
            refresh_token: refreshToken,
        };
    },
    
    convertToCodeChallenge(codeVerifier: string): string {
        const sha256 = new jssha('SHA-256', 'TEXT');
        sha256.update(codeVerifier);
        return sha256.getHash('B64').replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
    },

    errorHandler(exception: any): string {
        if (exception instanceof AxiosError) {
            const responseBody = exception.response?.data;
            return `${responseBody.error}: ${responseBody.error_description}`;
        }
        else {
            return exception.message;
        }
    },

}
