from core.granulation.granulizer import Granulizer
from core.granulation.granule import TextGranule
from core.similarity.sentence_similarity import compute_similarity
import numpy as np


class TextSumarizer(object):
    def __init__(self, granulizer: Granulizer):
        super().__init__()
        self.__granulizer = granulizer

    def summarize(self, text: str, ratio=0.01) -> str:
        granule = self.__granulizer.granulize(text)

        similarity_matrix = self._build_similarity_matrix(granule)
        sentences_scores = self._compute_scores(similarity_matrix)
        enumerated = list(enumerate(sentences_scores))
        enumerated.sort(key=lambda t: t[1])
        index = min(round(ratio * len(enumerated)), len(sentences_scores) - 1)

        extracted_sentences = enumerated[-index:]
        extracted_sentences.sort(key=lambda t: t[0])
        extracted_sentences = list(
            map(lambda t: granule.sentences_granules[t[0]], extracted_sentences))

        compressed_granule = TextGranule(extracted_sentences)
        return compressed_granule.to_string()

    def _build_similarity_matrix(self, granule) -> np.array:
        sentences = granule.sentences_granules
        l = len(sentences)
        m = np.zeros([l, l])
        for i in range(l):
            for j in range(l):
                if i == j:
                    continue
                m[i][j] = m[j][i] = compute_similarity(
                    sentences[i], sentences[j])

        norm = np.sum(m, axis=0)
        norm_m = np.divide(m, norm, where=norm != 0)
        return norm_m

    def _compute_scores(self, m: np.array) -> np.array:
        dc = 0.85       # so called damping coefficient
        thresh = 1e-5   # convergence threshold
        steps = 100
        scores = np.array([1] * len(m))

        p_sum = 0
        for step in range(steps):
            scores = (1 - dc) + dc * np.matmul(m, scores)
            if abs(p_sum - sum(scores)) < thresh:
                break
            else:
                p_sum = sum(scores)

        return scores
