builder.CreateFile("xlsx");
var oWorksheet = Api.GetActiveSheet();
oWorksheet.SetName("New worksheet name");
oWorksheet.GetRange("A1").SetValue("Just a text");
builder.SaveFile("xlsx", "SetName.xlsx");
builder.CloseFile();
