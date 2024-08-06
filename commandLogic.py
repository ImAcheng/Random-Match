import core

corefn = core.Core()

def ProcessCommand(command: str):
    # vars
    ArgsList: list = list(map(str, command.strip().split()))
    Arg0 = None
    Arg1 = None
    Arg2 = None

    # distribute args
    try:
        Arg0 = ArgsList[0]
        Arg1 = ArgsList[1]
        Arg2 = ArgsList[2]
    except IndexError:
        pass

    # process command
    match Arg0:
        case "add":
            if Arg1 == "name":
                corefn.AddNewStudent(Arg2)
            elif Arg1 == "object":
                corefn.AddNewObject(Arg2)

        case "remove":
            if Arg1 == "name":
                corefn.RemoveName(Arg2)
            elif Arg1 == "object":
                corefn.RemoveObject(Arg2)

        case "clear":
            corefn.clear(Arg1)

        case "match":
            corefn.Match()

        case "load":
            corefn.LoadFromData(Arg1, Arg2)