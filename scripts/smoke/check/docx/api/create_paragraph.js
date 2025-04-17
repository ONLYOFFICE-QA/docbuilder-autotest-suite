var oDocument = Api.GetDocument();
var oParagraph = oDocument.GetElement(0);
var text = oParagraph.GetText();
if (text != "This is a new paragraph") {
    console.log("Error: oParagraph.GetText() == " + text)
}
