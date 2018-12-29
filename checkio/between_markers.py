def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    begin_index = text.find(begin)
    end_index = text.find(end)
    # if begin_index >= end_index:
    #     return ''

    if begin_index == -1 and end_index == -1:
        return text
    elif begin_index == -1:
        return text[:end_index]
    elif end_index == -1:
        return text[begin_index+len(begin):]
    elif begin_index > end_index:
        return ""
    else:
        return text[begin_index+len(begin): end_index]





if __name__ == '__main__':

    print(between_markers('What is >apple<', '>', '<'))# == "apple", "One sym")
    print(between_markers("<head><title>My new site</title></head>", "<title>", "</title>"))# == "My new site", "HTML")
    print(between_markers('No[/b] hi', '[b]', '[/b]'))# == 'No', 'No opened')
    print(between_markers('No [b]hi', '[b]', '[/b]'))# == 'hi', 'No close')
    print(between_markers('No hi', '[b]', '[/b]'))# == 'No hi', 'No markers at all')
    print(between_markers('No <hi>', '>', '<'))# == '', 'Wrong direction')
