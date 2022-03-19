var mammoth = require("mammoth");
var path = require("path");

var filePath = path.join(__dirname,'./AlexAndreasResume.docx');

mammoth.extractRawText({path: filePath})
    .then(function(result){
        var text = result.value; // The raw text

        //this prints all the data of docx file
        //console.log(text);
        console.log('------------------------------');
        var textLines = text.split ("\n");

        for (var i = 0; i < textLines.length; i++) {
            //this prints all the data in separate lines
            console.log(textLines[i]);
        }
        var messages = result.messages;
    })
    .done();


