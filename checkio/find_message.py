def find_message(text: str) -> str:
    """Find a secret message"""

    input_keys = ""
    if text == text.upper():
        return text.replace("!","").replace(" ","")


    for i in range(0, len(text)):
        if text[i] == text[i].upper() and text[i].isalpha():
            input_keys += text[i]

    return input_keys


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))# == "HELLO", "hello"
    print(find_message("hello world!"))# == "", "Nothing"
    print(find_message("HELLO WORLD!!!"))# == "HELLOWORLD", "Capitals"

    print(find_message("A"))
    print(find_message("z"))
    #
    #
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

    str="sfgsdf"
    print(find_message("Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores."))
    print(find_message("dnwkldhiqw3ry37xhqdxaifiuoa7eya8w6r87a7y87y&Y&*DS&*DYH*&d8w9y8whd7*&Whdukjldwj*HDJKj"))
