/**
 * TODO Description
 */
$(document).ready(function () {
    // Store the computed style of the document.
    let style = getComputedStyle(document.body);

    // Iterate through each DOM element with the 'project-card-status-badge' class.
    $(".status-badge").each(function(index, element) {
        // Store the current element's text contents.
        let text = $(element).text();
        let color = 'transparent';

        // Set the background color of the current element based on it's text contents.
        if (text.startsWith('Future')) {
            color = style.getPropertyValue('--cool-gray');
        }
        else if (text.startsWith('In Progress')) {
            color = style.getPropertyValue('--deep-champagne');
        }
        else if (text.startsWith('Paused')) {
            color = style.getPropertyValue('--terra-cotta');
        }
        else if (text.startsWith('Completed')) {
            color = style.getPropertyValue('--green-sheen');
        }
        else {
            // If the current element's text field doesn't match a supported status, throw an exception.
            throw new Error('Error: Invalid project status; status: ' + text +
                ' at position: ' + (index + 1) + ' is not supported.');
        }

        // Set the element's background color to the determined color.
        $(element).css('background-color', color);
    });

    $('.repo-contents > .repo-item-separator:last-child').remove();


    // TODO Comments ...
    let detailColumn = $('#detail-column').data('currentProjectId', -1);

    // TODO Comments ...
    let shadowBox = $('#shadow-box').height($(document).height());

    // TODO Comments ...
    new ResizeSensor($('#list-column'), function() {
        shadowBox.height($('#list-column').outerHeight());
    });

    // TODO Comments ...
    $('.see-more-text').each(function (index, element) {
        $(element).addClass('not-hovering');
        $(element).mouseenter(function () {
            $(element).addClass('hovering').removeClass('not-hovering');
        }).mouseleave(function () {
            $(element).addClass('not-hovering').removeClass('hovering');
        }).click(function () {
            let projectCard = $(element).parent().parent().parent();
            $(".focused").removeClass('focused');
            projectCard.addClass('focused');

            let projectId = projectCard.data('projectId');

            let offsetTop = $('#' + projectId).offset().top;
            if (detailColumn.hasClass('expanded')) {
                $('html, body').animate({
                    scrollTop: offsetTop
                }, 300);
            } else {
                setTimeout(function () {
                    $('html, body').animate({
                        scrollTop: offsetTop
                    }, 300);
                    }, 300);
            }

            detailColumn.addClass('expanded').removeClass('collapsed');

            let currentProjectId = detailColumn.data('currentProjectId');

            if (projectId !== currentProjectId) {
                populateDetailColumn(projectId);
            }

            detailColumn.data('currentProjectId', projectId);
        });
    });

    // TODO Comments ...
    $('.exit-button').click(function () {
            $('.detail-container').addClass('hide').removeClass('show');
            shadowBox.addClass('hide-shadow').removeClass('show-shadow');
            setTimeout(function () {
                $('.detail-container').addClass('no-display');
                shadowBox.css('z-index', '-1')
                detailColumn.addClass('collapsed').removeClass('expanded');
                detailColumn.data('currentProjectId', -1);
                $(".focused").removeClass('focused');
            }, 300);
        });

    // TODO Comments ...
    function populateDetailColumn(projectId) {
        let current = $('.show').addClass('hide').removeClass('show');
        shadowBox.css('z-index', '1').addClass('show-shadow').removeClass('hide-shadow');
        setTimeout(function () {
            current.addClass('no-display');
            let container = $('.detail-container').filter(function (index, element) {
                return $(element).data('projectId') === projectId;
            }).removeClass('no-display');
            setTimeout(function () {
                container.addClass('show').removeClass('hide');
                }, 200);
            }, 200);
    }
});
