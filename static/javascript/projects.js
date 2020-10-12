/**
 * A fairly complex script which handles animations and the display of project details for the projects page. It also
 * dynamically sets the background color of project status badges based on their text.
 */

// Call a function when the document is ready to be displayed.
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

    // Remove excess repository item separators after the last repository item in each repository contents.
    $('.repo-contents > .repo-item-separator:last-child').remove();

    // Store the detail column DOM element and set it's current project ID to -1, meaning no current project.
    let detailColumn = $('#detail-column').data('currentProjectId', -1);

    // Store the shadow box DOM element and set it's height to that of the document.
    let shadowBox = $('#shadow-box').height($(document).height());

    // Create a new resize sensor to detect when the dimensions of the list column are changed.
    new ResizeSensor($('#list-column'), function() {
        // When the list column's dimensions have changed, update the height of the shadow box to that of the list
        // column.
        shadowBox.height($('#list-column').outerHeight());
    });

    // For each DOM element with the see-more-text CSS class, add a click event listener to focus its parent project
    // card and show the project's extended details in the detail column.
    $('.see-more-text').each(function (index, element) {
        // Store a reference to the current DOM element.
        let el = $(element);

        // Store a reference to the element's parent project card.
        let projectCard = el.parent().parent().parent();

        // Store the ID of the project associated with the project card.
        let projectId = projectCard.data('projectId');

        // Define a function to be executed when the element is clicked.
        el.click(function () {
            // Remove the focused CSS class from the currently focused project card, if any.
            $(".focused").removeClass('focused');

            // Add the focused CSS class to the current element's project card.
            projectCard.addClass('focused');

            // Store the amount of time, in milliseconds, to wait before performing a scroll animation and populating
            // the detail column.
            let pause = 0;

            // Check whether or not the detail column is currently expanded.
            if (detailColumn.hasClass('expanded')) {
                // If the detail column is currently expanded, immediately scroll the window to the calculated offset.
                $('html, body').animate({
                    scrollTop: $('#' + projectId).offset().top
                }, 300);
            } else {
                // Otherwise, expand the detail column.
                detailColumn.addClass('expanded').removeClass('collapsed');

                // Set the value of pause to 600 in order to wait 300 milliseconds after scrolling the window and before
                // populating the detail column with the project's details.
                pause = 600;

                // Wait 300 milliseconds to allow the detail column expand animation to finish first.
                setTimeout(function () {
                    // Scroll the window to the calculated offset.
                    $('html, body').animate({
                        scrollTop: $('#' + projectId).offset().top
                    }, 300);
                }, 300);
            }

            // Wait for the amount of time stored in pause before populating the detail column.
            setTimeout(function () {
                // If the project ID of the current project card differs from the current project id stored in the
                // detail column, populate the detail column with the current project's extended details.
                if (projectId !== detailColumn.data('currentProjectId')) {
                    populateDetailColumn(projectId);
                }
            }, pause);
        });
    });

    // Populate the detail column with the details of the project specified by its ID.
    function populateDetailColumn(projectId) {
        // Update the current project id stored in the detail column to that of the newly displayed project.
        detailColumn.data('currentProjectId', projectId);

        // Store a reference to the current detail container being displayed and hide it.
        let current = $('.show').addClass('hide').removeClass('show');

        // Store a reference to the new detail container to be displayed.
        let container = $('.detail-container').filter(function (index, element) {
                return $(element).data('projectId') === projectId;
        });

        // Disable the display of the current project details.
        current.addClass('no-display');

        // Enable the display of the new project details.
        container.removeClass('no-display');

        // Change the z-index of the shadow box to be above the non-focused project cards and start its fade-in
        // animation.
        shadowBox.css('z-index', '1').addClass('show-shadow').removeClass('hide-shadow');

        // Start new project details container's fade-in animation.
        container.addClass('show').removeClass('hide');
    }

    // For each DOM element with the exit-button CSS class, add a click event listener to collapse the detail column and
    // shadow box, and clean up other loose ends.
    $('.exit-button').click(function () {
        // Hide the detail container that is currently displayed in the detail column, if any.
        $('.detail-container').addClass('hide').removeClass('show');

        // Hide the shadow box.
        shadowBox.addClass('hide-shadow').removeClass('show-shadow');

        // Wait for the hide animations to finish, then call a function.
        setTimeout(function () {
            // Disable the display of the project details.
            $('.detail-container').addClass('no-display');

            // Change the z-index of the shadow box to be below the rest of the document.
            shadowBox.css('z-index', '-1')

            // Start the detail column collapse animation.
            detailColumn.addClass('collapsed').removeClass('expanded');

            // Set the current project id stored in the detail column to indicate that there is no current project.
            detailColumn.data('currentProjectId', -1);

            // Remove the focused CSS class from the previously focused project card.
            $(".focused").removeClass('focused');
        }, 400);
    });
});
