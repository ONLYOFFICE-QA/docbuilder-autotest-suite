builder.OpenFile("result.pptx");
var oPresentation = Api.GetPresentation();
var aSlides = oPresentation.GetAllSlides();
if (aSlides.length != 2) {
    console.log("Error: aSlides.length == " + aSlides.length);
}
builder.CloseFile();
