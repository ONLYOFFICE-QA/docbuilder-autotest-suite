var oDocument = Api.GetDocument();
var oParagraph = oDocument.GetElement(0);
var oRun = oParagraph.GetElement(0);
var text = oRun.GetText();
if (text != "This is a text run") {
    console.log("Error: oRun.GetText() == " + text)
}
