builder.CreateFile("xlsx");
var oWorksheet = Api.GetActiveSheet();
oWorksheet.GetRange("A1").SetValue("Just a text");
builder.SaveFile("xlsx", "GetActiveSheet.xlsx");
builder.CloseFile();
