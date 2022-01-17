$(document).ready(function () {

  $('#copy-decklist').tooltip();  
  $("#decklist-form").submit(function (event) {
    $("#form-submit").attr("disabled", true);
    $("#button-loaded").attr("hidden", true);
    $("#button-loading").attr("hidden", false);
    var formData = {
      url: $("#url").val(),
      format: $("#format").val(),
    };

    $.ajax({
      type: "GET",
      url: "/decklist/",
      data: formData,
      dataType: "json",
      encode: true,
      success: function (data) {
        $('#url').removeClass("is-invalid");
        $("#decklist-text").text(data.decklist);
        $("#decklist").attr("hidden", false);
      },
      error: function () {
        $('#url').addClass("is-invalid");
        $('#url-validation-feedback').text("Invald URL.");
      }
    }).always(function () {
      $("#form-submit").attr("disabled", false);
      $("#button-loading").attr("hidden", true);
      $("#button-loaded").attr("hidden", false);
    });

    event.preventDefault();
  });

  $('#copy-decklist').click(function() {
    navigator.clipboard.writeText($('#decklist-text').text());
    $('#copy-decklist').attr("disabled", true);
    $('#copy-decklist').text("Decklist Copied!");
  });
});