import docbuilder


def test_create_paragraph(builder):
    result_path = builder.build("scripts/docx/api/create_paragraph.js")
    builder = docbuilder.CDocBuilder()
    builder.OpenFile(result_path, "")
    context = builder.GetContext()
    global_obj = context.GetGlobal()
    api = global_obj["Api"]
    document = api.Call("GetDocument")
    assert document.Call("GetElement", 1).Call("GetText").ToString() == "This is a new paragraph"
    builder.CloseFile()


def test_create_run(builder):
    result_path = builder.build("scripts/docx/api/create_run.js")
    builder = docbuilder.CDocBuilder()
    builder.OpenFile(result_path, "")
    context = builder.GetContext()
    global_obj = context.GetGlobal()
    api = global_obj["Api"]
    document = api.Call("GetDocument")
    assert document.Call("GetElement", 1).Call("GetText").ToString() == "This is a text run"
    builder.CloseFile()
