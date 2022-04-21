def string_splosion(str_input):

    str_output = ""

    for i in range(len(str_input)):
        str_output = str_output + str_input[:i + 1]

    return str_output


print(string_splosion("Code"))
