# Portfolio Web Application System Design

## Overview

The Portfolio Web Application is designed to showcase Pradiv Gnanaraj's profile, a list of Python applications, and a contact form. The application is built using Streamlit, providing a user-friendly interface to interact with the content.

## Architecture

The architecture of the Portfolio Web Application comprises several components that work together to create an engaging user experience:

1. **Homepage (`home.py`):** This component forms the main landing page of the application. It displays a profile image, a brief introduction, and a list of Python applications. Information about the apps is retrieved from the `data.csv` file.

2. **Email Sending (`end_email.py`):** This component handles email sending using the `smtplib` library. The `send_email()` function is utilized to send emails, facilitating communication between users and Pradiv.

3. **Contact Form (`Contact_Us.py`):** This component implements the contact form feature. Users can input their email address, select a subject, write a message, and send it to Pradiv using the `send_email()` function.

4. **Data Files (`data.csv` and `topics.csv`):** These CSV files store information about Python apps and contact form subjects, respectively. The app information is used to populate the homepage, while the subjects are shown in the contact form dropdown.

5. **Images (`images/`):** This directory contains images used in the application, including the profile photo and images associated with the Python apps.

## Data Flow

1. Users access the Portfolio Web Application through a web browser.
2. The `home.py` script reads the `data.csv` file to display app information on the homepage.
3. Users can select the contact form in the `Contact_Us.py` script to input their details and send a message.
4. The `send_email()` function in the `end_email.py` script is used to send the message to Pradiv's email address.
5. Images for the profile photo and app images are loaded from the `images/` directory.

## File Structure

- `home.py`
- `end_email.py`
- `Contact_Us.py`
- `data.csv`
- `topics.csv`
- `images/` (Directory containing images)
- `LICENSE` (License file)
- `README.md` (Project documentation)

## Interaction Flow

1. User accesses the web application in their browser.
2. User lands on the homepage (`home.py`) and views Pradiv's profile and the list of apps.
3. User navigates to the contact form (`Contact_Us.py`), inputs their details, and sends a message.
4. The application uses the `send_email()` function to send the message to Pradiv's email address.

## Dependencies

- Python 3.x
- Streamlit
- Pandas

## Limitations and Future Enhancements

- Currently, the application focuses on showcasing apps and a contact form. Future enhancements could include personalized user accounts and more advanced user interactions.
- The design and layout can be improved to enhance the overall visual appeal of the application.

## Conclusion

The Portfolio Web Application demonstrates the integration of various components to create an interactive platform for users to learn about Pradiv Gnanaraj's profile and engage through a contact form. The architecture provides a solid foundation for future enhancements and improvements.

---

**Note:** This document provides a high-level overview of the Portfolio Web Application's system design. Customize the content based on your project's specifics.
