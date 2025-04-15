import docbuilder


def test_get_element(builder):
    result_path = builder.build("scripts/docx/api_document/get_element.js")
    builder = docbuilder.CDocBuilder()
    builder.OpenFile(result_path, "")
    context = builder.GetContext()
    global_obj = context.GetGlobal()
    api = global_obj["Api"]
    text = api.Call("GetDocument").Call("GetElement", 0).Call("GetText").ToString()
    print(f"Result: {text}")
    assert text == "This is just a sample text. Nothing special."
    builder.CloseFile()


def test_get_element2(builder):
    result_path = builder.build("scripts/docx/api_document/get_element.js")
    builder = docbuilder.CDocBuilder()
    builder.OpenFile(result_path, "")
    context = builder.GetContext()
    global_obj = context.GetGlobal()
    api = global_obj["Api"]
    text = api.Call("GetDocument").Call("GetElement", 0).Call("GetText").ToString()
    print(f"Result: {text}")
    assert text == "This is just a sample text. Nothing special."
    builder.CloseFile()


def test_get_element3(builder):
    result_path = builder.build("scripts/docx/api_document/get_element.js")
    builder = docbuilder.CDocBuilder()
    builder.OpenFile(result_path, "")
    context = builder.GetContext()
    global_obj = context.GetGlobal()
    api = global_obj["Api"]
    text = api.Call("GetDocument").Call("GetElement", 0).Call("GetText").ToString()
    print(f"Result: {text}")
    assert text == "This is just a sample text. Nothing special."
    builder.CloseFile()


def test_get_element4(builder):
    result_path = builder.build("scripts/docx/api_document/get_element.js")
    builder = docbuilder.CDocBuilder()
    builder.OpenFile(result_path, "")
    context = builder.GetContext()
    global_obj = context.GetGlobal()
    api = global_obj["Api"]
    text = api.Call("GetDocument").Call("GetElement", 0).Call("GetText").ToString()
    print(f"Result: {text}")
    assert text == "This is just a sample text. Nothing special."
    builder.CloseFile()
