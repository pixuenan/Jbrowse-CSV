String.format = function() {
  var s = arguments[0];
  for (var i = 0; i < arguments.length - 1; i++) {
  var reg = new RegExp("\\{" + i + "\\}", "gm");
  s = s.replace(reg, arguments[i + 1]);
  }
  return s;
};

function readTextFile(file)
{
  var rawFile = new XMLHttpRequest();
  var regionList = new Array();
  rawFile.open("GET", file, false);
  rawFile.onreadystatechange = function ()
  {
    if(rawFile.readyState === 4)
    {
      if(rawFile.status === 200 || rawFile.status == 0)
      {
        var allText = rawFile.responseText;
        var stringList = allText.split("\n");
        for (var line in stringList){
          var position = stringList[line];
          var chr = position.split(":")[0];
          var coordinate = parseInt(position.split(":")[1]);
          if (chr){
          var region = chr + ":" + (coordinate-100).toString() + "-" + (coordinate+100).toString();
          regionList.push(region);}
        }
      }
    }
  };
  rawFile.send(null);
  return regionList;
}


function buildTable(list, tableId) {
  // get the reference for the body
  var tbl = document.getElementById(tableId);
  var tblBody = document.createElement("tbody");
  for (var i=0;i<list.length; i++){
    var row = document.createElement("tr");
    var cell = document.createElement("td");

    var index = document.createElement("td");
    index.appendChild(document.createTextNode((i+1).toString()));

    var region = list[i];
    var link = document.createElement("a");
    link.setAttribute("href","#");
    link.setAttribute("onclick","igv.browser.search('"+region+"')");
    var linkText = document.createTextNode(region);
    link.appendChild(linkText);
    cell.appendChild(link);

    var annotation = document.createElement("input");
    annotation.setAttribute("type", "text");
    annotation.setAttribute("class", "form-control");

    row.appendChild(index);
    row.appendChild(cell);
    row.appendChild(annotation);

    tblBody.appendChild(row);
  }
  // put the <tbody> in the <table>
  tbl.appendChild(tblBody);
  // appends <table> into <body>
  body.appendChild(tbl);
  // sets the border attribute of tbl to 2;
  tbl.setAttribute("border", "2");
}
