/**
 * A JavaScript script which utilizes jQuery to dynamically set the background color of a project card's status badge
 * based on the status of the project. This action is applied when the DOM is ready.
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

        // TODO Description
        $(element).mouseover(function () {
            $(element).stop(true).animate( {
                backgroundColor: color,
                borderColor: color
            }, 100);
        }).mouseout(function () {
            $(element).stop(true).animate( {
                backgroundColor: jQuery.Color({ alpha: 0 }),
                borderColor: jQuery.Color(0, 0, 0, 1)
            }, 100);
        });
    });
});
