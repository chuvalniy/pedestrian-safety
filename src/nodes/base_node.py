from ..element.base_element import BaseElement
from ..element.video_end_break_element import VideoEndBreakElement
from ..element.frame_element import FrameElement


class BaseNode:
    def __init__(self):
        pass

    def process(self, element: BaseElement):
        if isinstance(element, VideoEndBreakElement):
            return element
        if not isinstance(element, FrameElement):
            raise TypeError(f"{self.__class__.__name__}: Input element is of incorrect type. "
                            f"Expected FrameElement, got {type(element).__name__}")
