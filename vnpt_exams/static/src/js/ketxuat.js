//------------------conver html to word-----------------------
function tableToWord() {
    $("#id_tbl").wordExport();
}
//------------------conver html to excel-----------------------
var tableToExcel = (function () {
    var uri = 'data:application/vnd.ms-excel;base64,'
        , template = '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40"><head><!--[if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>{worksheet}</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]--><meta http-equiv="content-type" content="text/plain; charset=UTF-8"/></head><body><table>{table}</table></body></html>'
        , base64 = function (s) {
        return window.btoa(unescape(encodeURIComponent(s)))
    }
        , format = function (s, c) {
        return s.replace(/{(\w+)}/g, function (m, p) {
            return c[p];
        })
    }
    return function (table, name, fileName) {
        if (!table.nodeType) table = document.getElementById(table)
        var ctx = {worksheet: name || 'Worksheet', table: table.innerHTML}
        //window.location.href = uri + base64(format(template, ctx))
        document.getElementById("dlink").href = uri + base64(format(template, ctx));
        document.getElementById("dlink").download = fileName;
        document.getElementById("dlink").click();
    }

})()

//------------------conver html to pdf-----------------------

var form = $('#id_tbl'),
    cache_width = form.width(),
    a4 = [841.89, 595.28];  // for a4 size paper width and height
var a_left = 10;
var a_right = 10;
var a_page = 'landscape';//One of 'a3', 'a4' (Default),'a5' ,'letter' ,'legal'

function converHTMLtoPDF() {
    $('body').scrollTop(0);
    createPDF();
}
function createPDF() {
    getCanvas().then(function (canvas) {
        var
            img = canvas.toDataURL("image/png"),
        //doc = new jsPDF({
        //  unit:'px',
        //  format:'a4'
        //});
            doc = new jsPDF(a_page);
        doc.addImage(img, 'JPEG', a_right, a_left);
        doc.save('KetxuatPdf.pdf');
        form.width(cache_width);
    });
}

// create canvas object
function getCanvas() {

    form.width((a4[0] * 1.33333) - 80).css('max-width', 'none');
    return html2canvas(form, {
        imageTimeout: 2000,
        removeContainer: true
    });
}

//---------------------------------in--------------------------------

function printTable() {
    printData()
}
function printData() {
    var divToPrint = document.getElementById("id_tbl");
    newWin = window.open("");
    newWin.document.write(divToPrint.outerHTML);
    newWin.print();
    newWin.close();
}