import core

corefn = core.Core()

def ProcessCommand(command: str):
    # vars
    ArgsList: list = list(map(str, command.strip().split()))

    # process command
    match ArgsList[0]:
        case "add":
            if ArgsList[1] == "name":
                corefn.AddNewStudent(ArgsList[2])
            elif ArgsList[1] == "object":
                corefn.AddNewObject(ArgsList[2])

        case "remove":
            if ArgsList[1] == "name":
                corefn.RemoveName(ArgsList[2])
            elif ArgsList[1] == "object":
                corefn.RemoveObject(ArgsList[2])

        case "clear":
            corefn.clear(ArgsList[1])

        case "match":
            corefn.Match()

        case "load":
            corefn.LoadFromData(ArgsList[1], ArgsList[2])