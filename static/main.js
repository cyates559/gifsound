$(function requestLinks() {
    $.ajax({
        type: "GET",
        url: "/api/links/somekeyzz",
        contentType: "application/json; charset=utf-8",
        success: function (data) {
            createColumnDef(JSON.parse(data));
        },
        error: function (jqXHR, textStatus, errorThrown) {
            alert(errorThrown);
        }
    });
});

function createColumnDef(data) {
    for (var i = 0; i < data.length; i++) {
        rowData.push({
            name: data[i].name,
            link: data[i].full_link,
            views: data[i].views,
            time_created: data[i].time_created
        });
    }
    console.log(rowData)
    console.log(data.length)
    console.log(data[0].name)
    var eGridDiv = document.querySelector('#myGrid');
    new agGrid.Grid(eGridDiv, gridOptions);
}
var rowData = [];

// define columns and grid options
var columnDefs = [
    {headerName: "Name", field: "name"},
    {headerName: "Link", field: "link"},
    {headerName: "views", field: "views"},
    {headerName: "Date Added", field: "time_created"}
];

var gridOptions = {
    columnDefs: columnDefs,
    rowData: rowData,
    enableFilter: true,
    enableSorting: true,
    animateRows: true,
    sortingOrder: ['desc', 'asc', null],
    onGridReady: function () {
        gridOptions.api.sizeColumnsToFit();
    }
};

function selectAllRows() {
    gridOptions.api.selectAll();
}

document.addEventListener("DOMContentLoaded", function () {
    // lookup the container we want the Grid to use


});