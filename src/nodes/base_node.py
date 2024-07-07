from element import (
    BaseElement,
    FrameElement,
    VideoEndBreakElement
)


class BaseNode:
    def __init__(self):
        pass

    def process(self, element: BaseElement):
        if isinstance(element, VideoEndBreakElement):
            return element

        assert isinstance(
            element, FrameElement
        ), f"{self.__name__} | Неправильный формат входного элемента {type(element)}"
