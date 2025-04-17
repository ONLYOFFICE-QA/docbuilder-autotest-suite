var oDocument = Api.GetDocument();
var oParagraph = oDocument.GetElement(0);
var text = oParagraph.GetText();
if (text != "This is just a sample text. Nothing special.") {
    console.log("Error: oParagraph.GetText() == " + text)
}
