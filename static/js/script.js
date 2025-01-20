document.querySelectorAll('.vote-button').forEach(button => {
    button.addEventListener('click', () => {
        const postId = button.getAttribute('data-post-id');
        const voteType = button.getAttribute('data-vote-type');
        
        // Get the CSRF token from the meta tag
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

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
            document.querySelector('.vote-button[data-vote-type="upvote"]').innerHTML = 
                `Upvote (${data.total_upvotes})`;
            document.querySelector('.vote-button[data-vote-type="downvote"]').innerHTML = 
                `Downvote (${data.total_downvotes})`;
        })
        .catch(error => {
            console.error('Error during voting:', error);
            alert('An error occurred while processing your vote.');
        });
    });
});