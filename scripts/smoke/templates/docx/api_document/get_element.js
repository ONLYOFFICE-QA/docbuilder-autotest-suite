builder.CreateFile("docx");
var oDocument = Api.GetDocument();
var oParagraph = oDocument.GetElement(0);
oParagraph.AddText("This is just a sample text. Nothing special.");
builder.SaveFile("docx", "GetElement.docx");
builder.CloseFile();
