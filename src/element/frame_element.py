from base_element import BaseElement
import numpy as np


class FrameElement(BaseElement):
    def __init__(
            self,
            source: str,
            frame: np.ndarray
    ):
        """
        :param source: Path to the processed video.
        :param frame: Video frame presented as numpy array
        """
        self.source = source
        self.frame = frame
