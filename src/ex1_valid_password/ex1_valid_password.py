class ValidPassword:
    def valid_password(self, password):
        if type(password) != str:
            raise ValueError('Password must be a string!')
        if len(password) < 8:
            return False
        upper = 0
        special = 0
        digit = 0
        for letter in password:
            if letter.isupper():
                upper += 1
            if letter in '!@#$%^&*(){}[]\\|:";\'<>?,./':
                special += 1
            if letter.isdigit():
                digit += 1
        if upper == 0 or special == 0 or digit == 0:
            return False
        else:
            return True
