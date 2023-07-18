if (!$.fn.DataTable.isDataTable("#myTable")) {
  $("#myTable").DataTable({
    paging: true,
    pagingType: "simple_numbers",
    pageLength: 3,
    lengthMenu: [5],
    bLengthChange: false,
    searching: true,
    language: {
      info: "",
      search: "",
    },
    ordering: false,
  });

  $("#search").keyup(function () {
    var table = $("#myTable").DataTable();
    table.search($(this).val()).draw();
  });
}

console.log("js file connected");
