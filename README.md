# Portfolio Web Application

This repository showcases a Streamlit-based web application that provides users with information about Pradiv Gnanaraj, including a portfolio of Python applications and a contact form.

## Files

1. `home.py`: This script creates the homepage of the portfolio web application using Streamlit. It displays a profile image, a brief introduction, and a list of Python apps built by Pradiv. The app information is read from a `data.csv` file, and images are loaded from the "images" folder.

2. `end_email.py`: This script handles sending emails using the `smtplib` library. It includes a function `send_email()` that takes a message and sends it to a specified email address. The email subject, sender's email, and message content are customizable.

3. `Contact_Us.py`: This script implements a contact form in the portfolio web application. Users can input their email address, select a subject from a dropdown list, and write a message. Upon submission, the message is sent to Pradiv's email address using the `send_email()` function.

4. `images/`: This folder contains images, including a profile photo and images associated with the Python apps.

5. `data.csv`: A CSV file that stores information about the Python apps in the portfolio. It includes columns for app title, description, image filename, and source code URL.

6. `topics.csv`: Another CSV file that contains topics for the contact form dropdown list.

## Usage

1. Install the required libraries: `streamlit`, `pandas`.
2. Run the Streamlit app using the command: `streamlit run home.py`.
3. Access the portfolio web application in your web browser by following the link provided by Streamlit.

## Features

- **Home Page**: The homepage introduces Pradiv Gnanaraj, showcasing a profile image and a brief introduction.
- **Python Apps**: The homepage displays a list of Python apps built by Pradiv. App information is read from `data.csv`.
- **Contact Form**: Users can send emails to Pradiv using the contact form in the `Contact_Us.py` script.
- **Modular Structure**: The project uses modular scripts for different functionalities, enhancing maintainability and code reusability.

## Dependencies

- Python 3.x
- Streamlit
- Pandas

## Future Enhancements

- Implement user authentication to provide personalized experiences.
- Enhance the design and layout of the portfolio web application.
- Expand the contact form to include more fields for user input.

## Contribution

Feel free to contribute to this project by submitting pull requests or suggesting improvements. Follow the coding conventions and maintain consistency with the existing code.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Streamlit and Pandas libraries for enabling the creation of interactive web applications.
- The Python community for continuous support and contributions.

---

**Note:** This `README.md` file provides an overview of the Portfolio Web Application project. Customize the content to match your project's specifics and provide clear instructions for users.
