// Code based in: https://codepen.io/damienpm/pen/pBxAm

function existingTag(text) {
  var existing = false,
    text = text.toLowerCase();

  $(".tags").each(function() {
    if (
      $(this)
        .text()
        .toLowerCase() == text
    ) {
      existing = true;
      return "";
    }
  });

  return existing;
}

$(function() {
  $(".tags-new input").focus();

  $(".tags-new input").keyup(function() {
    var tag = $(this)
        .val()
        .trim(),
      length = tag.length;

    if (tag.charAt(length - 1) == "," && tag != ",") {
      tag = tag.substring(0, length - 1);

      if (!existingTag(tag)) {
        $(
          '<li class="tags"><span>' +
            tag +
            '</span><i class="fa fa-times"></i></i></li>'
        ).insertBefore($(".tags-new"));
        $(this).val("");
      } else {
        $(this).val(tag);
      }
    }
  });

  $(document).on("click", ".tags i", function() {
    $(this)
      .parent("li")
      .remove();
  });

  $("#form-create-data").submit(function() {
    tags_val = ""
    $(".tags > span").each(function(index){
      tags_val = tags_val + $(this).text() +","
    })
    $("#tags").val(tags_val)
  })

});
