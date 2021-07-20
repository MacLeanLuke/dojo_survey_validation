from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

class Dojo():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']

    # create a new author
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"

        new_dojo_id = connectToMySQL('dojo_survey_schema').query_db(query, data)

        return new_dojo_id

    @classmethod
    def delete_dojo(cls, data):

        query = "DELETE FROM dojos WHERE id = %(id)s;"

        connectToMySQL('dojo_survey_schema').query_db(query, data)

    @classmethod
    def update_dojo(cls, data):

        # UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)

        query = "UPDATE dojos SET name = %(name)s, location = %(location)s, language = %(location)s, comment = %(comment)s WHERE id = %(id)s;"

        connectToMySQL('dojo_survey_schema').query_db(query, data)

    # return all authors
    @classmethod
    def get_dojo_by_id(cls, data):

        query = "SELECT * FROM dojos WHERE id = %(id)s;"

        results = connectToMySQL('dojo_survey_schema').query_db(query, data)

        # print(type(results))

        return results

    @staticmethod
    def validate_employee(data):

        name_regex = re.compile(r"^[A-Za-z- .,#']{1,45}$")

        is_valid = True

        if not name_regex.match(data['name']):
            flash("Name should be between one and forty-five characters.")
            is_valid = False

        if data['comment'] != '':
            if not name_regex.match(data['comment']):
                flash("Comment should be forty-five characters or less.")
                is_valid = False

        if not name_regex.match(data['location']):
            flash("Location should be between one and forty-five characters.")
            is_valid = False

        if not name_regex.match(data['language']):
            flash("Language should be between one and forty-five characters.")
            is_valid = False

        return is_valid

    

