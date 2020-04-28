$(document).ready(function () {
	let csrf_token = $("csrf_token").val();

	$.ajaxSetup({
		beforeSend: function (xhr, settings) {
			if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrf_token);
			}
		}
	});

	$('#registrationForm').on('submit', function(e) {
		e.preventDefault();

		$("#alert", "#name-error", "#email-error").hide();
		$("#alert").removeClass("alert-success").removeClass("alert-danger");
		$("#name", '#email').removeClass("is-invalid");

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