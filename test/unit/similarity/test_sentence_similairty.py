from core.granulation.granulizer import Granulizer
from core.similarity.sentence_similarity import compute_similarity


def test_similarity_function():
    granulizer = Granulizer()
    s1 = granulizer.create_sentence_granule(
        'The quick brown fox jumps over the lazy dog.')
    s2 = granulizer.create_sentence_granule(
        'The lazy dog jumps over the fence.')
    s3 = granulizer.create_sentence_granule(
        'The result of this process is a dense graph representing the document.')

    similarity_s1_s2 = compute_similarity(s1, s2)
    similarity_s1_s3 = compute_similarity(s1, s3)

    assert similarity_s1_s2 > similarity_s1_s3
