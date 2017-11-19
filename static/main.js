// specify the columns
var columnDefs = [
    {headerName: "Name", field: "name"},
    {headerName: "Link", field: "link"},
    {headerName: "Views", field: "views"}
];

var rowData = [
    {name: "Cat Meme", link: "www.example.com", views: 35000},
    {name: "LOL", link: "www.gs/api/yay", views: 32000},
    {name: "Doctors HATE HIM!", link: "www.google.com", views: 72000}
];

var gridOptions = {
    columnDefs: columnDefs,
    rowData: rowData,
    enableFilter: true,
    enableSorting: true,
    animateRows: true,
    sortingOrder: ['desc','asc',null],
    onGridReady: function () {
        gridOptions.api.sizeColumnsToFit();
    }
};

function selectAllRows() {
    gridOptions.api.selectAll();
}

document.addEventListener("DOMContentLoaded", function () {
    // lookup the container we want the Grid to use
    var eGridDiv = document.querySelector('#myGrid');

    // create the grid passing in the div to use together with the columns & data we want to use
    new agGrid.Grid(eGridDiv, gridOptions);
});