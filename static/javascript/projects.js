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

    // TODO Description ...
    $('#detail-column').data('currentProjectId', -1);

    // TODO Description ...
    $('.see-more-text').each(function (index, element) {
        $(element).addClass('not-hovering')
        $(element).mouseenter(function () {
            $(element).addClass('hovering').removeClass('not-hovering');
        }).mouseleave(function () {
            $(element).addClass('not-hovering').removeClass('hovering');
        }).click(function () {
            let projectId = $(element).parentsUntil('.project-card').parent().data('projectId');
            let detailColumn = $('#detail-column');
            let currentProjectId = detailColumn.data('currentProjectId');

            detailColumn.data('currentProjectId', projectId);
            detailColumn.addClass('expanded').removeClass('collapsed');

            setTimeout(function () {
                populateDetailColumn(projectId);
            }, 400)
        });
    });

    // TODO Description ...
    $('.exit-button').click(function () {
            $('.detail-container').addClass('hide').removeClass('show');
            setTimeout(function () {
                $('#detail-column').addClass('collapsed').removeClass('expanded');
            }, 400)
        });

    function populateDetailColumn(projectId) {
        $('.show').addClass('hide').removeClass('show');
        $('.detail-container').filter(function (index, element) {
            return $(element).data('projectId') === projectId;
        }).addClass('show').removeClass('hide');
    }
});
