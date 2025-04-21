builder.OpenFile("result.docx");
var oDocument = Api.GetDocument();
var oParagraph = oDocument.GetElement(0);
var text = oParagraph.GetText();
if (text != "This is just a sample text. Nothing special.\r\n") {
    console.log("Error: oParagraph.GetText() == " + text);
}
builder.CloseFile();
