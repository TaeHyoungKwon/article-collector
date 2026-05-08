from src.summarize import _parse_three_bullets


def test_parse_three_bullets_basic():
    text = "- 첫째\n- 둘째\n- 셋째"
    assert _parse_three_bullets(text) == ["첫째", "둘째", "셋째"]


def test_parse_three_bullets_truncates_extra():
    text = "- a\n- b\n- c\n- d"
    assert _parse_three_bullets(text) == ["a", "b", "c"]


def test_parse_three_bullets_strips_numbering():
    text = "1. 첫째\n2. 둘째\n3. 셋째"
    assert _parse_three_bullets(text) == ["첫째", "둘째", "셋째"]


def test_parse_three_bullets_handles_no_marker():
    text = "첫째 줄\n둘째 줄\n셋째 줄"
    assert _parse_three_bullets(text) == ["첫째 줄", "둘째 줄", "셋째 줄"]


def test_parse_three_bullets_skips_blank_lines():
    text = "\n- 첫째\n\n- 둘째\n\n- 셋째\n"
    assert _parse_three_bullets(text) == ["첫째", "둘째", "셋째"]
