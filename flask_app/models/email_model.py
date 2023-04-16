from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, EMAIL_REGEX
from flask import flash


class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # add a single email into the emails table
    @classmethod
    def add_email(cls, data):
        query = """
            INSERT INTO emails( email )
            VALUES ( %(email)s )
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    
    @classmethod
    def get_all_emails(cls, data):
        query = """
            SELECT *
            FROM emails
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # method to validate the email
    @staticmethod
    def validate_email(email_entry):
        is_valid = True
        if not EMAIL_REGEX.match(email_entry['email']):
            flash("Please provide a valid email address.", 'error_email')
            is_valid = False
        return is_valid
