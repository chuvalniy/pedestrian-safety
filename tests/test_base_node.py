import pytest
import numpy as np
from src.element.frame_element import FrameElement
from src.element.video_end_break_element import VideoEndBreakElement
from src.nodes.base_node import BaseNode


@pytest.fixture()
def mock_frame_element():
    test_source = "test_source"
    test_frame = np.empty(0)

    test_element = FrameElement(test_source, test_frame)
    return test_element


@pytest.fixture()
def mock_video_end_break_element():
    test_source = "test_source"

    test_element = VideoEndBreakElement(test_source)
    return test_element


def test_base_node(mock_frame_element, mock_video_end_break_element):
    base_node = BaseNode()

    # process FrameElement
    base_node.process(mock_frame_element)

    # process VideoEndBreakElement
    base_node.process(mock_video_end_break_element)
