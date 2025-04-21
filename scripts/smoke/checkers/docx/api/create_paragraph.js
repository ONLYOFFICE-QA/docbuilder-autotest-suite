builder.OpenFile("result.docx");
var oDocument = Api.GetDocument();
var aParagraphs = oDocument.GetAllParagraphs();
var text = aParagraphs[1].GetText();
if (aParagraphs.length != 2) {
    console.log("Error: aParagraphs.length == " + aParagraphs.length);
}
if (text != "This is a new paragraph") {
    console.log("Error: oParagraph.GetText() == " + text);
}
builder.CloseFile();
