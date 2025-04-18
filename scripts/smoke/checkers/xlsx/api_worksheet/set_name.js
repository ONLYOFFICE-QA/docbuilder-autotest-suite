var oWorksheet = Api.GetSheet("New worksheet name");
var text = oWorksheet.GetRange("A1").GetText();
oWorksheet.SetName();
if (text != "Just a text") {
    console.log("Error: GetRange(A1).GetText() == " + text)
}
