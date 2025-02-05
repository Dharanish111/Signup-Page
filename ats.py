import streamlit as st

def main():
    st.image("https://www.astrolitetech.com/assets/img/logo.png")

    st.title("Signup")

    # Input fields for user information
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    # Checkbox for terms and conditions
    terms_accepted = st.checkbox("I agree to the terms and conditions")

    # Error messages (initially empty)
    username_error = ""
    email_error = ""
    password_error = ""
    confirm_password_error = ""
    terms_error = ""

    if st.button("Sign Up"):
        # Validation logic
        if not username:
            username_error = "Username is required."
        if not email:
            email_error = "Email is required."
        elif "@" not in email:  # Basic email validation. For more robust validation, use a library
            email_error = "Invalid email format."
        if not password:
            password_error = "Password is required."
        if password != confirm_password:
            confirm_password_error = "Passwords do not match."
        if not terms_accepted:
            terms_error = "You must accept the terms and conditions."

        # If no errors, proceed with signup
        if not username_error and not email_error and not password_error and not confirm_password_error and not terms_error:
            # Simulate storing user data (replace with actual database interaction)
            # For demonstration, just print the user data
            print(f"New user: {username}, {email}, {password}")  # Replace with database storage

            st.success(f"Signup successful! Welcome, {username}!")  # Include username in success message

        else:
            # Display error messages
            st.error(username_error)
            st.error(email_error)
            st.error(password_error)
            st.error(confirm_password_error)
            st.error(terms_error)


if __name__ == "__main__":
    main()