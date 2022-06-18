
$(document).on("submit", "#form", function(e){
                        e.preventDefault();


               $.ajax({
                    type: "POST",
                    url: "/",
               data: {
                    email: $("#email").val(),
                    title: $("#title").val(),
                    text: $("#text").val(),
               csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
               },
               error: function(response){
                alert("error")
               }
               });
               let name = document.getElementById("div")
               name.innerHTML = '<div class="alert alert-warning alert-dismissible fade show" role="alert"><strong>Message has been sent!</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
});


