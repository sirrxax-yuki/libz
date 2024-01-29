import User from '@/models/schema/libz/User';

export default interface SearchRequest {
    user: User,
    keyword: string,
}
