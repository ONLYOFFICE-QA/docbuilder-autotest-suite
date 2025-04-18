var oWorksheet = Api.GetActiveSheet();
var text = oWorksheet.GetRange("A1").GetText();
if (text != "Just a text") {
    console.log("Error: GetRange(A1).GetText() == " + text)
}
