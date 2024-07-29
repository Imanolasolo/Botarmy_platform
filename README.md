# README.md for Botarmy Hub Platform

## Overview

The **Botarmy Hub Platform** is a web application built using Streamlit that provides a variety of services for users interested in AI-based tool development. This platform offers different user tiers, each with unique features and access levels. Users can log in to access tailored resources based on their roles or enter as a guest to explore introductory content.

## Features

- **User Authentication**: Secure login system with user roles including Admin, Basic, Premium, Developer, and Guest.
- **Role-Based Access**: Different functionalities and resources are available based on the user's role.
- **Guest Access**: Limited access for users who want to explore the platform without logging in.
- **Informative UI**: Clear navigation and information about the services provided by the platform.

## Installation

To run the Botarmy Hub Platform, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Imanolasolo/botarmy_hub_platform.git
   cd botarmy_hub_platform
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Then, install the required packages:
   ```bash
   pip install streamlit
   ```

3. **Prepare User Data**:
   Create a `users.json` file in the root directory of the project. This file should contain user data in the following format:
   ```json
   [
       {"name": "admin", "password": "adminpass", "role": "admin"},
       {"name": "user1", "password": "user1pass", "role": "basic"},
       {"name": "user2", "password": "user2pass", "role": "premium"},
       {"name": "dev", "password": "devpass", "role": "developer"}
   ]
   ```

4. **Run the Application**:
   Start the Streamlit server by running:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Access the Platform**:
   Open your web browser and navigate to `http://localhost:8501`.

2. **Login**:
   - Enter your username and password in the sidebar.
   - Click the "LOGIN" button to authenticate.
   - If you do not have an account, you can enter as a guest by clicking "Enter as Guest".

3. **Explore Services**:
   Once logged in, you will be redirected to your respective dashboard based on your role. Each role has specific features and resources available.

## User Roles and Services

- **Admin**: Full access to all features and administrative controls.
- **Basic**: Access to basic AI development tools and resources.
- **Premium**: Access to advanced tools and premium support.
- **Developer**: Collaboration tools and resources for AI project development.
- **Guest**: Limited access to introductory resources and information.

## Contributing

Contributions are welcome! If you would like to contribute to the Botarmy Hub Platform, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for providing an excellent framework for building web applications.
- All contributors and users for their support and feedback.
