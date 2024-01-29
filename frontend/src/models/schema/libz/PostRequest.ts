import User from '@/models/schema/libz/User';

export default interface PostResponse {
    user: User,
    keywords: string[],
    knowledge: string,
    knowledge_type: string,
    private: boolean,
}
