builder.CreateFile("xlsx");
var oWorksheet = Api.GetActiveSheet();
oWorksheet.GetRange("A1").SetValue("Just a text");
oWorksheet.SetName("New worksheet name");
builder.SaveFile("xlsx", "SetName.xlsx");
builder.CloseFile();
