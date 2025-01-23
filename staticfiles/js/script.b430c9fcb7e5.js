// Ensure DOM content is fully loaded before adding event listeners
document.addEventListener('DOMContentLoaded', () => {
    // Select all vote buttons
    document.querySelectorAll('.vote-button').forEach(button => {
        button.addEventListener('click', () => {
            const postId = button.getAttribute('data-post-id');
            const voteType = button.getAttribute('data-vote-type');

            // Get the CSRF token from the meta tag
            const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

            // Validate necessary attributes
            if (!postId || !voteType) {
                console.error('Missing data-post-id or data-vote-type attribute');
                alert('Invalid vote action. Please refresh and try again.');
                return;
            }

            // Make a POST request to the vote endpoint
            fetch(`/post/vote/${postId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken // Include the CSRF token in the headers
                },
                body: JSON.stringify({ vote_type: voteType })
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    // Check for expected response structure
                    if (data.total_upvotes === undefined || data.total_downvotes === undefined) {
                        throw new Error('Unexpected response structure.');
                    }

                    // Update vote button text
                    document.querySelector('.vote-button[data-vote-type="upvote"]').innerHTML =
                        `Upvote (${data.total_upvotes})`;
                    document.querySelector('.vote-button[data-vote-type="downvote"]').innerHTML =
                        `Downvote (${data.total_downvotes})`;

                    // Optionally, display a success message
                    alert('Your vote has been recorded successfully!');
                })
                .catch(error => {
                    console.error('Error during voting:', error);
                    alert('An error occurred while processing your vote. Please try again later.');
                });
        });
    });
});