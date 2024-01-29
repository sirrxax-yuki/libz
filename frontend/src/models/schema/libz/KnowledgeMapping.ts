import Knowledge from '@/models/schema/libz/Knowledge';

export default interface KnowledgeMapping {
    keywords: readonly string[],
    knowledge: Knowledge,
}
