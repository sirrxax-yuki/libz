import User from '@/models/schema/libz/User';

export default interface DeleteRequest {
    user: User,
    knowledge_id: number,
}
