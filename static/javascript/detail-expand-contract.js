/*
$(".project-card").each(function(index, element) {
        $(element).mouseover(function () {
            $('#detail-column').stop(true).animate( {
                maxWidth: '40%'
            }, 300);
        });
        $(element).mouseout(function () {
            console.log($(element).prop('width'));
            console.log($(element).prop('max-width'));
            if ($(element).prop('width') === $(element).prop('max-width')) {
                setTimeout(function () {
                    if ($(element).prop(':hover'))
                        return

                    // TODO Handle canceling the animation if any of the other project cards is hovered over.

                    $('#detail-column').stop(true).animate( {
                        maxWidth: '0%'
                    }, 300);
                }, 2000);
            } else {
                $('#detail-column').stop(true).animate({
                    maxWidth: '0%'
                }, 300);
            }
        });
    });
 */

/**
 * TODO Description
 */
/*
$(document).ready(function () {
    $(".project-card").each(function(index, element) {
        $(element).mouseover(function () {
            $('#detail-column').stop(true).animate( {
                maxWidth: '40%'
            }, 300);
        });
    });
});
 */
