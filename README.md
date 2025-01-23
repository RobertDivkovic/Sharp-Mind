# Sharp Mind

[Link to live page](https://newssharpmind-7fe060023557.herokuapp.com/)


![alt text]()

## Table of Contents
- [Introduction](#introduction)
- [User Experience (UX)](#user-experience-ux)
  - [Strategy Plane](#strategy-plane)
  - [Scope Plane](#scope-plane)
  - [Structure Plane](#structure-plane)
  - [Skeleton Plane](#skeleton-plane)
  - [Surface Plane](#surface-plane)
- [Existing Features](#existing-features)
- [User Flows](#user-flows)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## Introduction

Sharp-Mind is a dynamic platform where users can create accounts, log in, and interact by posting, reading, and commenting on various topics. This project aims to provide a user-friendly environment for content sharing and discussion. The platform covers multiple categories, ensuring inclusivity and diverse content.

# UX - User Experience Design
A user experience designer, Jesse James Garrett, introduced five UX design elements in his book *The Elements of User Experience*. In the book, he explains the steps of user experience projects and what UX designers should consider at each stage. This is where most of my planning process steps came from.

The 5 planes of UX are as below:

- **The Strategy Plane**
- **The Scope Plane**
- **The Structure Plane**
- **The Skeleton Plane**
- **The Surface Plane**

The UX of the Sharp-Mind blog application was meticulously designed and implemented following the Five Planes of UX methodology by Jesse James Garrett. Below is a detailed breakdown of each plane and how it applies to the Sharp-Mind project:

## Strategy Plane

The foundation of Sharp-Mind's UX revolves around understanding its purpose, identifying user needs, and defining business goals.

### Purpose: 

Sharp-Mind is designed to serve as an intuitive platform where users can share, explore, and discuss topics of interest. The goal is to encourage meaningful interactions and foster a sense of community.

### User Needs:

#### Primary Users:
- Casual readers looking for trending or specific category-based content.
- Contributors who want to publish and manage posts.
- Engaged community members interested in commenting and interacting.
#### Key Needs:
- Simple navigation to browse categories and trending posts.
- A smooth post-creation process with text formatting capabilities.
- An intuitive interface for commenting and responding to posts.
- Secure login, registration, and profile management features.

### Business Goals:

- Encourage user engagement through content sharing and interactions.
- Build a scalable platform that can be enhanced with features like collaboration requests and staff communication.
- Provide seamless integration with tools like Cloudinary for image management.


## Scope Plane

This defines the features and functionality offered by Sharp-Mind.

### Content Features:

- Categorized posts for easier browsing.
- Trending posts based on user engagement (voting activity).
- Rich-text formatting and image upload capabilities for posts.
- Commenting system with upvote/downvote functionality.

### Interactive Features:

- User authentication (registration, login, logout).
- Profile management (edit profile picture via Cloudinary).
- Real-time feedback through Django messages for form submissions and errors.

### Non-functional Requirements:

- Mobile-responsive design for a seamless experience across devices.
- Secure HTTPS connections with proper security settings.
- Optimized performance for faster page loads (via tools like Whitenoise and caching).

## Structure Plane

The structure plane of Sharp-Mind defines how the content and features are organized, ensuring users can easily navigate and achieve their goals.

### Information Architecture
The platform organizes content logically and intuitively to provide an optimal user experience.

#### Homepage:

- Displays a Welcome Section with a prominent heading, encouraging exploration.
- Categories Section: Collapsible menu listing all available categories for browsing posts by topic.
- Trending Posts Section: Highlights the most popular posts based on user engagement (votes and comments).
- Post Feed: Displays a list of the latest posts with titles, excerpts, and categories. Each post links to its detailed page.
- Pagination allows users to navigate through additional posts.

#### Profile Page:

- Displays user-specific information, such as their username, profile picture, and a list of posts created by them.
- Post Management: Users can edit or delete their posts directly from this page.
- Profile Editing Options: Provides the ability to upload a new profile picture using Cloudinary integration.

#### Post Detail Page:

- Includes the post's title, content, featured image, and metadata (author, published date, categories).

- Comment Section:
- Displays approved comments in chronological order.
- Logged-in users can add new comments, view pending comments (for moderation), and edit/delete their comments.

- Voting Section:
- Buttons for upvoting and downvoting posts, displaying the total number of votes.

#### About Page:

- Explains the purpose of Sharp-Mind and its mission to foster meaningful discussions.
- Includes a summary of the platform's features and benefits for both readers and contributors.
- Provides a call-to-action encouraging visitors to register and join the community.

#### Contact Page:

- Features a Get in Touch Form that allows users to contact the team with questions, feedback, or to report a problem.
- Includes fields for name, email, subject, and message.
- Uses Django messages to provide real-time feedback after form submission (e.g., success or error messages).

## User Flows
Detailed pathways outlining how users interact with the platform to accomplish their goals.

### New User Flow:
1) Access Website: Navigate to the homepage.
2) Register: Click "Register" in the navbar and complete the signup form.
3) Login: After registration, log in using the "Login" button in the navbar.
4) Explore Posts: Browse categories, trending posts, or the main feed to find interesting posts.
5) Interact: Comment on posts, upvote or downvote, and share insights.

### Post Creation Flow:

1) Login: Ensure the user is authenticated.
2) Navigate to Create Post: Click the "Publish Your Post" button on the homepage.
3) Fill Out the Form: Provide a title, content, featured image, categories, and an optional excerpt.
4) Submit the Post: Click "Submit," and Django messages confirm success or display errors.
5) View Post: Redirected to the newly created post's detail page.

### Comment Flow:

1) Login: Ensure the user is logged in.
2) View Post: Navigate to a post's detail page.
3) Leave a Comment: Fill in the comment box and submit the form.
4) Moderation: Comment may appear as "Pending" until approved by the admin.
5) Edit/Delete Comment: Users can modify or remove their comments if needed.

### Profile Management Flow:

1) Login: Ensure the user is authenticated.
2) Access Profile: Click "Profile" in the navbar.
3) Edit Profile:
- Update the profile picture via an upload form connected to Cloudinary.
- View and manage previously created posts (edit or delete them).
4) Save Changes: Confirm updates and view real-time feedback through Django messages.

### Browsing Categories Flow:

1) Homepage Navigation: Access the collapsible "Categories" menu.
2) Select a Category: Click on a category to filter posts related to that topic.
3) Explore Posts: View all posts tagged with the selected category.

### Trending Posts Flow:

1) Homepage Navigation: Access the collapsible "Trending Posts" menu.
2) Explore Posts: Click on any trending post to view its detailed page.
3) Engage: Upvote, comment, or interact with the post as desired.

### Contact Us Flow:

1) Access Contact Page: Click "Contact" in the navbar.
2) Fill Out Form: Provide name, email, subject, and message.
3) Submit: Click the "Submit" button and receive feedback through Django messages.
4) Admin Interaction: Admins receive the message and respond appropriately.

### About Page Flow:

1) Access About Page: Click "About" in the navbar.
2) Learn About Sharp-Mind: Read the mission statement, features, and benefits.
3) Call-to-Action: Register to join the community and contribute.

## Skeleton Plane

### Wireframes and Layout
The wireframes for Sharp-Mind define the spatial arrangement and hierarchy of elements on key pages. Below are the detailed descriptions of each page's layout:

### Homepage

- Header (Sticky Navbar):
- Positioned at the top of the page.
- Includes the "Sharp-Mind" logo on the left and navigation links (Home, About, Contact, Login/Register or Profile/Logout) aligned to the right.
- A collapsible menu is included for responsiveness on smaller screens.

### Main Content Area:

- Welcome Heading: A large, centered <h1> element with a short welcome message.
- Categories Section: Collapsible sidebar or dropdown menu for category navigation on the left-hand side.
- Trending Posts Section: Another collapsible sidebar or dropdown menu showcasing top posts based on voting activity.

- Posts Feed:
- List of posts displayed as cards, arranged in a grid or vertical format.
- Each card contains:
- Featured image (or placeholder if none exists).
- Title (clickable to navigate to the post detail page).
- Excerpt (summary of the post content).
- Metadata (published date and associated categories as badges).
- Pagination at the bottom to navigate through multiple pages of posts.

### Post Detail Page

- Header: Same as the homepage for consistency.
- Main Content Area:
- Post Title: Bold and prominent at the top.
- Author and Published Date: Positioned below the title in smaller, muted text.
- Post Content: Full content of the post with embedded images or videos if applicable.
- Featured Image: Displayed prominently above or alongside the post content.
- Voting Buttons:
- Two buttons (Upvote and Downvote) styled distinctly for clarity.
- Displays the current vote count.
- Comment Section:
- Displays existing comments in reverse chronological order.
- Comment form for logged-in users to add new comments.
- Back to Homepage Button: Positioned at the bottom for easy navigation back to the homepage.

### Profile Page

- Header: Same as other pages for consistency.
- Main Content Area:
- User Information:
- Profile picture at the top (editable).
- Username and bio (if applicable).
- User Posts:
- List of posts created by the user.
- Each post is displayed with an edit and delete option.
- Edit Profile Form:
- Allows users to upload a new profile picture.
- Optionally allows editing other profile details like bio or email.

### About Page

- Header: Standard navbar.
- Main Content Area:
- Mission Statement: Large heading summarizing the purpose and goals of Sharp-Mind.
- Features List: Key features of the platform outlined in a visually appealing format (e.g., icons with descriptions).
- Call-to-Action: A button encouraging users to sign up and join the community.
- Contact Page
- Header: Standard navbar.
- Main Content Area:
- Get in Touch Form:
- Fields for Name, Email, Subject, and Message.
- Submit button styled to stand out.
- Success/Failure Messages:
- Real-time feedback provided via Django messages.

### Navigation and Interaction Design

- Responsive Navbar:

- Ensures access to key pages regardless of the device size.
- Collapsible on smaller screens to save space.
- Active link styling provides visual feedback to indicate the current page.

- Forms:

- Use of Django Crispy Forms ensures clean and consistent styling.
- Simplified layouts with clear labels and placeholders for ease of use.
- Real-time feedback on errors or successful submissions.

- Pagination:

- Positioned centrally at the bottom of the post feed for easy navigation.
- Clear active page indicator and hover effects for visual clarity.

### UI Interaction Flow

- Hover Effects:

- Links and buttons change color or add an underline effect on hover for better visual feedback.
- Cards slightly elevate on hover to indicate interactivity.
- Collapsible Sections:

- Categories and Trending Posts are hidden in dropdown menus to save space.
- Clickable headers expand and collapse these sections.
- Mobile Responsiveness:

- All elements are designed to adjust dynamically for different screen sizes.
- The navbar collapses into a toggler icon, and the layout of posts and sidebars stacks vertically on smaller screens.
 
### Accessibility Enhancements

-Contrast Ratios:

- High contrast between text and background colors ensures readability.
- Buttons and links are distinct from surrounding text.
- Keyboard Navigation:

- Users can navigate through links and forms using the keyboard (e.g., Tab key).

- ARIA Attributes:

- Used for collapsible elements like dropdowns and buttons to ensure compatibility with screen readers.


## Surface Plane
The surface plane is the visual design of Sharp-Mind, including its color scheme, typography, and imagery.

### Color Scheme:

### Primary Colors:
- Dark Blue (#34495e) for the header and footer, symbolizing reliability and professionalism.
- Light Grey (#f2f5f7) for the background to ensure readability and reduce visual strain.

### Accent Colors:

- Olive for hover states on pagination and interactive elements.
- Light Blue for links and buttons to provide a vibrant and engaging feel.

### Typography:

- Font Family: 'Roboto' from Google Fonts is used for its modern and clean appearance.
- Font Weights:
- Bold for headings and buttons to emphasize key areas.
- Regular for body text for improved readability.

### Imagery:

- Placeholder images for posts that lack a featured image, ensuring uniformity in design.
- Cloudinary is used to handle all media uploads securely.

### Responsiveness:

- Mobile-first design with collapsible navigation menus.
- Dynamic resizing of elements to fit screens below 768px width.

## How It Works

- User Authentication: Users can register and log in to the platform. Once logged in, they gain access to features like viewing detailed content of other users, creating posts, commenting, and viewing their profiles.
- Post Creation: Users can publish posts under different categories and include images. Each post is assigned a unique slug.
- Interactions: Users can:
- Upvote or Downvote: Show appreciation or disapproval of posts.
- Comment on Posts: Foster discussions by leaving comments.
- Profile Management: Logged-in users can access their personalized profile page to:
- View and manage their posts.
- See a history of their comments.
- Review their upvoted and downvoted posts.
- Collaboration Requests: Users can fill out and submit a Collaboration Request form. This allows them to propose working together with the platform or other users on specific topics, themes, or projects.
- Get in Touch: Sharp-Mind provides a Contact Us form where users can reach out to staff for support, suggestions, or inquiries. This ensures a direct communication channel between users and the administrative team.

## Existing Features
Sharp-Mind incorporates a wide range of features that enhance user interaction and streamline the blogging experience:
-	User Registration and Authentication: Users can securely sign up, log in, and log out of the platform. Once logged in, they gain access to all platform functionalities.
-	Create, View, Edit, and Delete Posts: Registered users can create posts, add images, and provide detailed content. They can also edit or delete their posts at any time.
-	Post Categorization and Filtering: Users can assign categories to their posts, making them more discoverable. On the homepage, users can filter and browse posts by categories for targeted exploration.
-	Trending Posts Section: The homepage displays a Trending Posts section based on a custom algorithm that calculates "trending scores" using the voting activity (upvotes and comments). This feature helps highlight popular and engaging content.
-	Voting System: Users can upvote or downvote posts to express approval or disapproval. The total number of upvotes and downvotes is displayed on each post.
-	Commenting: Users can leave comments on posts to engage in discussions. They can also edit or delete their comments.
-	Profile Management: Each user has a personalized profile page where they can:
-	View and manage their posts.
-	Review their comment history.
-	Access a list of upvoted and downvoted posts.
-	Collaboration Requests: Users can submit collaboration requests to propose projects or partnerships. This fosters community engagement and teamwork.
-	Contact Form: A dedicated Contact Us page allows users to reach out to staff for support, feedback, or inquiries.
-	Responsive Design: Sharp-Mind is fully responsive and provides a seamless experience on devices of all screen sizes.
-	Admin Functionality: The administrative dashboard allows admins to manage posts, comments, users, and categories efficiently.


## Technologies Used
Below is a comprehensive list of the technologies, frameworks, and tools used in developing the Sharp-Mind project:

### Languages

- Python: The core programming language used for backend logic and server-side functionalities.
- HTML5: For structuring the content and layout of the application.
- CSS3: For styling and designing the frontend, ensuring a responsive and visually appealing user interface.
- JavaScript: Used for dynamic frontend interactions and functionality (e.g., collapsible menus, voting buttons).

### Frameworks and Libraries

- Django (v4.2.18): Python-based web framework used for building the backend, handling routing, and managing the database.
- Bootstrap 5: Frontend framework for responsive design and pre-built components (e.g., modals, buttons, grids).
- Django-Allauth (v0.57.0): Library used for user authentication, registration, and account management.
- Django-Summernote (v0.8.20.0): WYSIWYG editor for rich text fields in posts.
- Django-Crispy-Forms (v2.0): For creating clean, responsive forms with enhanced usability.
- Crispy-Bootstrap5 (v0.7): Integration of Crispy Forms with Bootstrap 5 for improved form styling.
- Gunicorn (v20.1): Python WSGI HTTP server used for deploying the application in production.

### Database

- PostgreSQL: Relational database system used in production for secure, scalable, and efficient data management.
- SQLite: Lightweight database used for local development and testing.

### APIs and External Services

- Cloudinary: For hosting, managing, and serving images dynamically, including profile pictures and featured images.
- Font Awesome: Icon library used for navigation and branding elements.

### Tools

- Git: Version control system for tracking changes and collaborating on the project.
- GitHub: Repository hosting platform used to store and manage the project’s codebase.
- Heroku: Cloud-based platform for deploying, managing, and scaling the application in production.
- Am I Responsive?: Tool used to check the responsiveness of the web application across different devices.
- Lighthouse: Google tool used for auditing the performance, accessibility, and best practices of the application.
- VS Code: Code editor used for development with extensions for Python, Django, and Git integration.

### Package Management

- pip: Python package manager used to install dependencies and libraries.
- WhiteNoise (v5.3.0): For serving static files efficiently in production.

### Development Environment

- Code Institute’s Gitpod Workspace: An online IDE (Integrated Development Environment) used to develop and test the application.

### Browser Compatibility

The application has been tested and is compatible with the following browsers:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari

### Hosting

- Heroku Eco Dynos: Used for hosting the deployed application with a focus on cost-efficiency and sustainability.

### Other Utilities

- Django-Database-URL (v0.5): Library for configuring the database via environment variables.
- Psycopg2 (v2.9): PostgreSQL adapter for Python used to connect Django with PostgreSQL.
- Cloudinary-Storage: Django library for seamless integration with Cloudinary for media management.

## Testing
The Sharp-Mind project underwent extensive testing to ensure functionality, usability, and responsiveness. Below is a detailed breakdown of the testing conducted.

### Manual Testing

- Functionality Testing
- Each feature was tested manually to ensure it works as intended:

1) Navigation Bar:

- Verified that links (Home, About, Contact, Register, Login, Profile, Logout) direct users to the correct pages.
- Checked responsiveness for different screen sizes (mobile, tablet, desktop).
- Confirmed dropdown menus collapse and expand appropriately.

2) Authentication:

- Register: Ensured users can register with valid credentials and receive error messages for invalid inputs.
- Login: Tested login functionality for existing users and invalid credentials.
- Logout: Confirmed users are logged out and redirected to the home page.

3) Post Management:

- Create Post: Verified users can create a post with a title, content, image, categories, and an excerpt.
- Edit Post: Confirmed users can edit their posts and changes are reflected immediately.
- Delete Post: Ensured users can delete their posts with a confirmation prompt.

4) Commenting System:

- Checked users can submit comments.
- Verified pending comments are visible only to the author and are flagged for approval.
- Confirmed approved comments are visible to all users.

5) Voting System:

- Tested upvotes and downvotes functionality.
- Verified the trending score calculation is accurate and updates dynamically.

6) Contact Form:

- Confirmed users can submit messages through the form.
- Ensured error messages are displayed for missing or invalid input fields.

7) Search and Filtering:

- Verified users can search for posts by title or content.
- Tested category-based filtering to display only relevant posts.

### Edge Case Testing

- Attempted submitting a post with missing fields (e.g., no title or content) to ensure validation errors are shown.
- Tested file uploads with invalid formats (e.g., non-image files for featured images) and verified appropriate error handling.
- Checked how the application handles duplicate categories, posts, or comments.

### Responsive Design Testing

The website's responsiveness was tested on the following devices:

- Mobile Devices: Samsung S24 Ultra, Samsung A53, Samsung A35, iPhone 12, Samsung Galaxy S21, Google Pixel 5.
- Tablets: iPad Air, Samsung Galaxy Tab.
- Desktops/Laptops: 2560x1440, 1920x1080, 1366x768 resolutions.

- Tools Used:

- Google Chrome DevTools: Simulated different screen sizes.
- Am I Responsive?: Checked how the website renders on various devices.
- Lighthouse: Evaluated responsiveness score.

- Results:

- The application maintains usability across all devices.
- Dropdown menus, collapsible elements, and forms adapt seamlessly to smaller screens.
- Pagination is centered and functional for all resolutions.

### Automated Testing

- Django Tests
Unit tests were written to validate critical functionalities:

- Models:
- Verified data integrity for Post, Comment, Profile, and Category models.
- Checked the calculate_trending_score method for accuracy.

- Views:

- Tested CRUD operations for posts and comments.
- Verified access control (e.g., only authenticated users can create posts or comments).

- Forms:
- Ensured validation for PostForm, CommentForm, and ContactForm.
- Checked required fields trigger errors when empty.

- Example Test Cases:

- Create a post and confirm it appears on the home page.
- Submit an invalid comment and verify the error message.
- Check that anonymous users cannot access the profile or post creation pages.

### Lighthouse Testing

- Conducted performance, accessibility, and best practices audits using Google's Lighthouse tool.

- Results:

- Performance: Scored 85/100 after optimizing images and reducing render-blocking scripts.
- Accessibility: Achieved 100/100 by ensuring proper semantic HTML and ARIA labels.
- Best Practices: Improved to 95/100 by addressing HTTPS warnings and mixed content issues.

### User Feedback and Testing

- Testing Participants:

- Target Audience: Individuals interested in blogging and discussing various topics.
- Participants included 5 volunteers with varying technical expertise.

- Testing Tasks:

- Register, log in, and create a new post.
- Add a comment to an existing post.
- Use the category filter to find specific topics.
- Submit a message via the Contact form.
- Test responsiveness by resizing the browser window.

### Browser Compatibility Testing

- Tested on the following browsers:

- Google Chrome: Fully functional.
- Mozilla Firefox: Fully functional.
- Microsoft Edge: Fully functional.
- Safari: Fully functional.

### Bug Fixes
- Mixed Content Warnings: Resolved by enforcing HTTPS for all external resources (e.g., Cloudinary images).
- Pagination Misalignment: Fixed by centering the pagination in CSS.
- Comment Approval Issue: Addressed a bug where pending comments appeared public.

### Conclusion
Through rigorous testing, the Sharp-Mind project has achieved a high standard of functionality, usability, and responsiveness. Continuous feedback and iterative improvements have ensured the application provides an excellent user experience across devices and browsers.