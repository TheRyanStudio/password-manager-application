import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton, QStackedWidget, QWidget, QLineEdit, QTableWidget, QTableWidgetItem
from PySide6.QtCore import QFile, QIODevice  
from user_manager import User, UserManager
from encryption_utils import EncryptionUtils
from db_manager import DBManager

#NOTE: Works but will be refactored for readability and maintainability!

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_name = "main_window.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)

    loader = QUiLoader()
    widget = loader.load(ui_file, None)
    ui_file.close()

    if not widget:
        print(loader.errorString())
        sys.exit(-1)

    # -- Widgets --
    stack = widget.findChild(QStackedWidget, "stackMain")
    page_landing = widget.findChild(QWidget, "pageLanding")
    page_signup = widget.findChild(QWidget, "pageSignup")
    page_login = widget.findChild(QWidget, "pageLogin")
    page_dashboard = widget.findChild(QWidget, "pageDashboard")
    page_add_password = widget.findChild(QWidget, "pageAddPassword")

    table_entries_widget = widget.findChild(QTableWidget, "tableEntriesWidget")


    table_entries_widget.setColumnCount(3)
    table_entries_widget.setHorizontalHeaderLabels(["Organization", "Username", "Password"])

    # Enable stacked widget and set initial page
    stack.setEnabled(True)
    stack.setCurrentWidget(page_landing)

    #Helper func to clear inputs
    def clear_inputs(inputs):
        for i in inputs:
            i.clear()


    # --- Buttons ---
    btn_signup_page = widget.findChild(QPushButton, "btnSignupPage")
    btn_login_page = widget.findChild(QPushButton, "btnLoginPage")
    btn_signup = widget.findChild(QPushButton, "btnSignup")
    btn_login = widget.findChild(QPushButton, "btnLogin")
    btn_back_signup = widget.findChild(QPushButton, "btnBackSignup")
    btn_back_login = widget.findChild(QPushButton, "btnBackLogin")
    btn_logout = widget.findChild(QPushButton, "btnLogout")
    btn_add_password_page = widget.findChild(QPushButton, "btnAddPasswordPage")
    btn_cancel_add_password = widget.findChild(QPushButton, "btnCancelAddPassword")
    btn_delete_user = widget.findChild(QPushButton, "btnDeleteUser")
    btn_add_password = widget.findChild(QPushButton, "btnAddPassword")
    btn_reveal_passwords = widget.findChild(QPushButton, "btnRevealPasswords")

    # -- LineEdit --
    signup_email_input = widget.findChild(QLineEdit, "textSignupEmail")
    signup_password_input = widget.findChild(QLineEdit, "textSignupPassword")
    login_email_input = widget.findChild(QLineEdit, "textLoginEmail")
    login_password_input = widget.findChild(QLineEdit, "textLoginPassword")
    organization_input = widget.findChild(QLineEdit, "textOrganization")
    username_input = widget.findChild(QLineEdit, "textUsername")
    password_input = widget.findChild(QLineEdit, "textPassword")

    # Enable buttons
    btn_signup_page.setEnabled(True)
    btn_login_page.setEnabled(True)
    btn_signup.setEnabled(True)
    btn_login.setEnabled(True)
    btn_back_login.setEnabled(True)
    btn_back_signup.setEnabled(True)
    btn_logout.setEnabled(True)
    btn_add_password_page.setEnabled(True)
    btn_cancel_add_password.setEnabled(True)
    btn_delete_user.setEnabled(True)
    btn_add_password.setEnabled(True)
    btn_reveal_passwords.setEnabled(True)
    
    # Set button functions with an anonymous function
    btn_signup_page.clicked.connect(lambda: stack.setCurrentWidget(page_signup))
    btn_login_page.clicked.connect(lambda: stack.setCurrentWidget(page_login))
    btn_back_signup.clicked.connect(lambda:  (clear_inputs([signup_email_input, signup_password_input]), stack.setCurrentWidget(page_landing)))
    btn_back_login.clicked.connect(lambda: (clear_inputs([login_email_input, login_password_input, password_input]), stack.setCurrentWidget(page_landing)))
    
    btn_add_password_page.clicked.connect(lambda: stack.setCurrentWidget(page_add_password))

    btn_cancel_add_password.clicked.connect(lambda: (clear_inputs([organization_input, username_input, password_input]), stack.setCurrentWidget(page_dashboard)))
                                            

    # Initialize SQLlite Managers
    user_manager = UserManager()  
    db_manager = DBManager()

    # Enable tracking for the current user
    user_manager.current_user = None  

    # |- Handle Signup --
    def handle_signup():
        email = signup_email_input.text().strip()
        master_password = signup_password_input.text().strip()

        if not email or not master_password:
            print("Entries cannot be empty")
            return

        try:
            # Use EncryptionUtils to hash password
            encrypt_util = EncryptionUtils(master_password)

            user = User(email, encrypt_util.hash_password(), encrypt_util.salt)
            user_manager.add_user(user)
            print(f"User {email} signed up successfully!")

            clear_inputs([signup_email_input, signup_password_input])

            # Switch to login page after signup
            stack.setCurrentWidget(page_login)
        except Exception as e:
            print(f"Error signing up: {e}")

    btn_signup.clicked.connect(handle_signup)
    # -- Handle Signup -|

    # |- Handle Login --  
    def handle_login():
        email = login_email_input.text().strip()
        master_password = login_password_input.text().strip()

        if not email or not master_password:
            print("Entries cannot be empty")
            clear_inputs([login_email_input, login_password_input])
            return

        user_data = user_manager.get_user_by_email(email)
        if not user_data:
            print("No user found with that email")
            clear_inputs([login_email_input, login_password_input])
            return

        # Use EncryptionUtils to verify
        encrypt_util = EncryptionUtils(master_password, salt=user_data["salt"])
        if encrypt_util.verify_password(user_data["password_hash"]):
            print(f"User {email} logged in successfully!")
            
            user_manager.current_user = user_data

            # Stored temporarily while user is logged in 
            user_manager.current_key = encrypt_util.fernet
            clear_inputs([login_email_input, login_password_input])
            
            current_user_id = user_manager.current_user["user_id"]
            user_entries = db_manager.get_entries(current_user_id)



            for entry in user_entries:
                #decrypt each entry
                decrypted_entry = encrypt_util.decrypt(entry)
                row = table_entries_widget.rowCount()
                table_entries_widget.insertRow(row)
                table_entries_widget.setItem(row, 0, QTableWidgetItem(decrypted_entry["organization"]))
                table_entries_widget.setItem(row, 1, QTableWidgetItem(decrypted_entry["username"]))
                
            # Mask the password
                masked_password = "•" * len(decrypted_entry["password"])
                table_entries_widget.setItem(row, 2, QTableWidgetItem(masked_password))

            stack.setCurrentWidget(page_dashboard)
        else:
            clear_inputs([login_email_input, login_password_input])
            print("Incorrect password")

        

    btn_login.clicked.connect(handle_login)
        # -- Handle Login -|

    def handle_logout():
        user_email = user_manager.current_user["email"]
        user_manager.current_user = None
        user_manager.current_key = None


        # Clear table entries
        table_entries_widget.setRowCount(0)
        print(f"User {user_email} logged out.")
        stack.setCurrentWidget(page_landing)

    btn_logout.clicked.connect(handle_logout)

    def handle_delete_user():
        # Retrieve current user id
        current_user_id = user_manager.current_user["user_id"]
        current_user_email = user_manager.current_user["email"]
    
    
        user_manager.delete_user(current_user_id)
        print(f"User {current_user_email} was deleted.")
        user_manager.current_user = None    
        user_manager.current_key = None
        # Clear table entries
        table_entries_widget.setRowCount(0)
        stack.setCurrentWidget(page_landing)
    btn_delete_user.clicked.connect(handle_delete_user)   
    
    # |- Handle Add Password -- 
    def handle_add_password():
        organization = organization_input.text().strip()
        username = username_input.text().strip()
        password = password_input.text().strip()
        
        if not organization or not username or not password:     
            print("Entries cannot be empty")
            return
        
        # Retrieve current user id
        current_user_id = user_manager.current_user["user_id"]

        # Initialize EncryptionUtils with current logged in users fernet object
        encrypt_util = EncryptionUtils(fernet=user_manager.current_key)

        # Prepare data to encrypt
        entry_data = {
            "organization": organization,
            "username": username,
            "password": password
        }

        # Encrypt the data
        encrypted_entry = encrypt_util.encrypt(entry_data)
        encrypted_entry["user_id"] = current_user_id  

        db_manager.create_entry(encrypted_entry)
        print("Password entry added securely!")

        #Add entry to dashboard
        row = table_entries_widget.rowCount()
        table_entries_widget.insertRow(row)
        table_entries_widget.setItem(row, 0, QTableWidgetItem (entry_data["organization"]))
        table_entries_widget.setItem(row, 1, QTableWidgetItem(entry_data["username"]))
            
        # Mask the password
        masked_password = "•" * len(entry_data["password"])
        table_entries_widget.setItem(row, 2, QTableWidgetItem(masked_password))


        clear_inputs([organization_input, username_input, password_input])
        
        stack.setCurrentWidget(page_dashboard)   
    
    btn_add_password.clicked.connect(handle_add_password)
    # |- Handle Add Password -| 


    def handle_reveal_entries():
        current_user_id = user_manager.current_user["user_id"]
        encrypt_util = EncryptionUtils(fernet=user_manager.current_key)

        table_entries_widget.setRowCount(0)
        
        # Load all current user's entries from DB
        user_entries = db_manager.get_entries(current_user_id) 
        for entry in user_entries:
            # decrypt each entry
            decrypted = encrypt_util.decrypt(entry)  
            row = table_entries_widget.rowCount()
            table_entries_widget.insertRow(row)
            table_entries_widget.setItem(row, 0, QTableWidgetItem(decrypted["organization"]))
            table_entries_widget.setItem(row, 1, QTableWidgetItem(decrypted["username"]))
            table_entries_widget.setItem(row, 2, QTableWidgetItem(decrypted["password"]))

    btn_reveal_passwords.clicked.connect(handle_reveal_entries)


    widget.show()
    sys.exit(app.exec())