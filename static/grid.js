document.addEventListener("DOMContentLoaded", function () {
    var columnDefs = [
        {headerName: "Name", field: "name"},
        {headerName: "Link", field: "full_link"},
        {headerName: "views", field: "views"},
        {headerName: "Date Added", field: "time_created"}
    ];

    var gridOptions = {
        columnDefs: columnDefs,
        enableFilter: true,
        enableSorting: true,
        animateRows: true,
        sortingOrder: ['desc', 'asc', null],
        onGridReady: function () {
            gridOptions.api.sizeColumnsToFit();
            gridOptions.api.showLoadingOverlay()
        }
    };

    var eGridDiv = document.querySelector('#myGrid');
    new agGrid.Grid(eGridDiv, gridOptions);

    jsonLoad(function(data) {
        gridOptions.api.setRowData(data);
    })
});

function selectAllRows() {
    gridOptions.api.selectAll()
}


function jsonLoad(callback) {
        $.ajax({
            type: "POST",
            url: "/api/links",
            contentType: "application/json; charset=utf-8",
            success: function (data) {
                callback(JSON.parse(data));
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });
}



