import string_splitter

def test_split_empty_string_result_empty_array():
    # arrange
    stringToSplit = ""
    regex = ""
    expResult = []
    result = None
    cut = string_splitter.TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult