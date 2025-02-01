from abc import ABC, abstractmethod
class userauthentication(ABC):
    @abstractmethod
    def login(self,credentials):
        pass
    @abstractmethod
    def logout(self):
        pass
class googleauth(userauthentication):
    def login(self,credentials):
        print(f"attempting google login with credentials: {credentials}")
        if "google_token" in credentials and credentials["google_token"] == "valid_google_token":
            print("google login successfully")
            return True
        else:
            print("invalid google credentials")
            return False
    def logout(self):
        print("logging out from google")
        print("google logout successful")
        return True
class facebookauth(userauthentication):
    def login(self,credentials):
        print(f"attempting facebook login with credentials: {credentials}")
        if "facebook_token" in credentials and credentials["facebook_token"] == "valid_facebook_token":
            print("facebook login successful")
            return True
        else:
            print("invalid facebook credentials")
            return False
    def logout(self):
        print("logging out from facebook")
        print("facebook logout successful")
        return True
google_auth = googleauth()
facebook_auth = facebookauth()
google_credentials = {"google_token": "valid_google_token"}
facebook_credentials = {"facebook_token": "invalid_facebook_token"}
if google_auth.login(google_credentials):
    print("google login successful")
if not facebook_auth.login(facebook_credentials):
    print("facebook login failed")
google_auth.logout()
facebook_auth.logout()
    