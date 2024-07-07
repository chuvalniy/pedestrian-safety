from base_element import BaseElement


class VideoEndBreakElement(BaseElement):
    """
    Video stream interrupt element
    """

    def __init__(
            self,
            source: str
    ):
        """
        :param source: Path to the processed video.
        """
        self.source = source
