# Introduction 
Capstone Project Code Summary
Project Overview
Project Name: MovieReviews
Objective: A web application for managing and reviewing movies. The application allows users to view, create, edit, and delete movie reviews, with features for pagination, search, and a user-friendly interface.

1. User Stories & Implementation
      User Story 1: Basic Setup
      •	Objective: Create a new Django application with a basic home page.
      •	Implementation:
          o Created a Django project and an application named MovieReviews.
          o Developed a home page with basic content.
      User Story 2: Displaying a List of Items
      •	Objective: Display a list of movie items on a page.
      •	Implementation:
          o	Created a view items_list to retrieve and display movie items.
          o	Implemented pagination to handle large lists of movies.
          o	Added a search feature to filter movies by title.
          o	Created a template items_list.html to render the list of movies with pagination controls.
      User Story 3: Item Details
       •	Objective: Show detailed information for a single movie item.
       •	Implementation:
          o	Created a view item_details to display details of a selected movie.
          o	Implemented a template item_details.html to show movie details.
          o	Added functionality for editing and deleting items with appropriate links.
     User Story 4: Editing Items
      •	Objective: Allow users to edit movie details.
      •	Implementation:
          o	Created a view item_edit to handle movie editing with a form.
          o	Added a template item_edit.html with a form for updating movie details.
          o	Integrated form handling to update movie records in the database.
      User Story 5: Deleting Items
      •	Objective: Allow users to delete a movie and confirm deletion.
      •	Implementation:
          o	Created a view item_delete to handle item deletion.
          o	Added a template item_delete.html with a confirmation form for deletion.
          o	Displayed a success message after successful deletion using Django messages framework.

   2. Code Components
      Models
        •	File: models.py
        •	Description: Defines the Movie model with fields for title, description, rating, and release date.
      Views
        •	File: views.py
        •	Description: Contains logic for handling requests and rendering templates.
      Templates
        •	File: base.html
          o	Description: Base template with common layout and styles.
      •	File: item_details.html
          o	Description: Template for displaying movie details with edit and delete options.
      •	File: item_delete.html
          o	Description: Template for confirming item deletion
      Static Files
      •	File: styles.css
          o	Description: Custom styles for the application.
      •	File: scripts.js
          o	Description: JavaScript functions for sticky headers, smooth scrolling, masonry layout, and slider.
          URLs
      •	File: urls.py
      •	Description: Defines URL patterns and maps them to views.
  3. How to Run the Project
      1.	Install Dependencies: Ensure you have Python and Django installed. Run pip install -r requirements.txt to install dependencies.
      2.	Run Migrations: Apply database migrations with python manage.py migrate.
      3.	Start the Server: Run the development server with python manage.py runserver.
      4.	Access the Application: Open http://127.0.0.1:8000/ in your web browser.

4. Conclusion
This summary provides an overview of the capstone project, detailing the user stories implemented, key code components, and instructions for running the application. For a complete view of the code, please refer to the repository on GitHub.




