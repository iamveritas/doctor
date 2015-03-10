/*
* Приховує поле місце роботи і показує його, коли вибрано місто
* */
$(document).ready(function () {
    $("div.dl-horizontal").has("#id_hospitals").hide();
    $("#id_city").on('change blur', function() {
        var city = $("#id_city").val();
        var request = "city=" + city;
        $.get("/doctors/ajax_test/", request, function(data) {
            $("#id_hospitals").html(data.hospitals)
        });
        $("div.dl-horizontal").has("#id_hospitals").show();
   });
});
