import hmac

class CustomTokenGenerator:
    def make_token(self, user):
        """
        Override the make_token method to create a token without timestamp.
        """
        # Include user ID in the token
        return self._make_hash_value(user)

    def _make_hash_value(self, user):
        """
        Generate a hash that includes user's ID, user's last_login,
        and the timestamp to create a unique token.
        """
        return hash(user.pk) 
    
    def check_token(self, user, token):
        """
        Check if the token matches the expected token for the user.
        """
        expected_token = self.make_token(user)
        print('type of expected token is',type(expected_token))
        return hmac.compare_digest(token, str(expected_token))



custom_token_generator = CustomTokenGenerator()
