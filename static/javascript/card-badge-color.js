/**
 * A JavaScript script which utilizes jQuery to dynamically set the background color of a project card's status badge
 * based on the status of the project. This action is applied when the DOM is ready.
 */
$(document).ready(function(){
    // Store the computed style of the document.
    let style = getComputedStyle(document.body);

    // Iterate through each DOM element with the 'project-card-status-badge' class.
    $(".project-card-status-badge").each(function(index, element) {
        // Store the current element's text contents.
        let text = $(element).text();

        // Set the background color of the current element based on it's text contents.
        if (text.startsWith('Future')) {
            this.style.background = style.getPropertyValue('--purple-pale');
        }
        else if (text.startsWith('In Progress')) {
            this.style.background = style.getPropertyValue('--yellow-light');
        }
        else if (text.startsWith('Paused')) {
            this.style.background = style.getPropertyValue('--gray-darker');
        }
        else if (text.startsWith('Completed')) {
            this.style.background = style.getPropertyValue('--yellow-green');
        }
        else {
            // If the current element's text field doesn't match a supported status, throw an exception.
            throw new Error('Error: Invalid project status; status: ' + text +
                ' at position: ' + (index + 1) + ' is not supported.');
        }
    });
});
