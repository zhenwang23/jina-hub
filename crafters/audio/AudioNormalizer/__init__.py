import numpy as np
from jina.executors.crafters import BaseCrafter


class AudioNormalizer(BaseCrafter):
    """
    :class:`AudioNormalizer` normalizes the audio signal on doc-level..
    """

    def craft(self, blob: np.ndarray, *args, **kwargs):
        """
        Reads the `ndarray` of the audio signal, normalizes the signal and saves the `ndarray` of the normalized signal
        in the `blob` of the Document.

        :param blob: the ndarray of the audio signal
        :return: a Document dict with the normalized audio signal
        """
        import librosa

        signal_norm = librosa.util.normalize(blob)

        return dict(offset=0, weight=1.0, blob=signal_norm)
