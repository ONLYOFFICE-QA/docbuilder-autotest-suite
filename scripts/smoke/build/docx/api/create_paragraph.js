var oDocument = Api.GetDocument();
var oParagraph = Api.CreateParagraph();
oParagraph.AddText("This is a new paragraph");
oDocument.Push(oParagraph);
