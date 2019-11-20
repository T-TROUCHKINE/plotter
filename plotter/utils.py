def wrap_str(string, width):
    lines = [""]
    string = string.split()
    for word in string:
        if (len(lines[-1])+len(word)) > width:
            lines.append(word)
        else:
            if len(lines[-1]) > 0:
                lines[-1] += " " + word
            else:
                lines[-1] += word
    return "\n".join(lines)
