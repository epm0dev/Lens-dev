/**
 * TODO Description
 */

// TODO Description
$(document).ready(function () {
    let settings = {
        contentWidth: $(window).width(),
        verticalGutter: 0,

    };
    let pane = $('.flex-wrapper').jScrollPane(settings);

    pane.bind(
        'jsp-scroll-y',
        function (event, scrollYPositionY, isAtTop, isAtBottom) {
            console.log('pee')
        }
    )
});
