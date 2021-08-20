// Sidenav
$(document).ready(function () {
	$(".sidenav").sidenav({
		edge: "right"
	});
	$('select').formSelect();

	validateMaterializeSelect();

	function validateMaterializeSelect() {
		let classValid = {
			"border-bottom": "1px solid #4caf50",
			"box-shadow": "0 1px 0 0 #4caf50"
		};
		let classInvalid = {
			"border-bottom": "1px solid #f44336",
			"box-shadow": "0 1px 0 0 #f44336"
		};
		if ($("select.validate").prop("required")) {
			$("select.validate").css({
				"display": "block",
				"height": "0",
				"padding": "0",
				"width": "0",
				"position": "absolute"
			});
		}
		$(".select-wrapper input.select-dropdown").on("focusin", function () {
			$(this).parent(".select-wrapper").on("change", function () {
				if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
					$(this).children("input").css(classValid);
				}
			});
		}).on("click", function () {
			if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
				$(this).parent(".select-wrapper").children("input").css(classValid);
			} else {
				$(".select-wrapper input.select-dropdown").on("focusout", function () {
					if ($(this).parent(".select-wrapper").children("select").prop("required")) {
						if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
							$(this).parent(".select-wrapper").children("input").css(classInvalid);
						}
					}
				});
			}
		});
	}
});


/* Show Image Preview
    Sourced from http://jsfiddle.net/2d7axmdr */
function recipeImg() {
	// For recipes
	$(".new-img").css("display", "flex");
	$(".current-img").css("display", "none");
	var url = $("#recipe_img").val();
	$('.img-window').attr('src', url);
}


//Back to top btn
//Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
	scrollFunction();
};

function scrollFunction() {
	if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
		mybutton.style.display = "block";
	} else {
		mybutton.style.display = "none";
	}
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
	document.body.scrollTop = 0; // For Safari
	document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}