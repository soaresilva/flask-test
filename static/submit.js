$(document).ready(function () {
// include CSRF token header
	let csrf_token = $("csrf_token").val();

	$.ajaxSetup({
		beforeSend: function (xhr, settings) {
			if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrf_token);
			}
		}
	});

// grabs form ID to do the call
	$('#registrationForm').on('submit', function(e) {
		e.preventDefault();

// hiding existent bootstrap classes/success/error divs when clicking submit button
		$("#alert, #name-error, #email-error").hide();
		$("#alert, #name-error, #email-error").html("");
		$("#alert").removeClass("alert-success").removeClass("alert-danger");
		$("#name, #email").removeClass("is-invalid");

// grabbing form data and sending it via post
// showing useful response messages to the user via bootstrap classes
		$.post({
			data : $(this).serialize(),
			type : 'POST',
			url : '/'
		})
		.done(function (data) {
			$("#alert").html(data.message).addClass("alert-success").show();
		})
		.fail(function (error) {
            let message = $.parseJSON(error.responseText).message;
            if(error.status == 400) {
                for (key in message) {
                    let errorLabel = $("#" + key + "-error");
                    $("#"+key).addClass("is-invalid");
                    if (errorLabel !== null) {
                        errorLabel.html(message[key]).show();
                    } else {
                        finalMessage += key + ": " + message[key];
                    }
                }
            } else if (error.status == 500) {
                $("#alert").html(message).addClass("alert-danger").show();
                }
		});
		return false;
	});
});
