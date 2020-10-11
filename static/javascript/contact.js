/**
 * A small script which sets the height and width of the message overlay DOM element to the height and width of the
 * document, respectively.
 */

// Call a function when the document is ready to be displayed.
$(document).ready(function () {
    // Select and store the message overlay DOM element with jQuery.
    let overlay = $('#message-overlay');

    // If the message overlay was found in the DOM tree, set it's height and width to the height and width of the
    // document, respectively.
    if (overlay) {
        overlay.height($(document).height());
        overlay.width($(document).width());
    }
});
