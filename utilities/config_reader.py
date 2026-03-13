import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ConfigReader:

    @staticmethod
    def get_homeurl():
        return config.get("app_urls", "home_url")

    @staticmethod
    def get_loginurl():
        return config.get("app_urls", "login_url")

    @staticmethod
    def get_registrationurl():
        return config.get("app_urls", "regi_url")

    @staticmethod
    def get_hometitle():
        return config.get("titles", "home_title")


    @staticmethod
    def get_signupheading():
        return config.get("titles", "signup_heading")

    @staticmethod
    def get_dashboard_heading():
        return config.get("titles", "dashboard_heading")

    @staticmethod
    def get_regi_page_heading():
        return config.get("titles", "regipage_heading")

    @staticmethod
    def get_edit_user_page_heading():
        return config.get("titles", "edit_user_heading")

    @staticmethod
    def get_user_management_heading():
        return config.get("titles", "user_management_heading")

    @staticmethod
    def get_username():
        return config.get("login_data", "user_name")

    @staticmethod
    def get_password():
        return config.get("login_data", "password")

    @staticmethod
    def get_search_username():
        return config.get("login_data", "search_user")

    @staticmethod
    def get_temp_password():
        return config.get("login_data", "set_password")

    @staticmethod
    def get_excel_file_name():
        return config.get("test_data_file", "filename")

    @staticmethod
    def get_excel_sheet_name():
        return config.get("test_data_file", "sheetname")
