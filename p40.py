from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self, credentials):
        pass

class PasswordAuthentication(Authentication):
    def __init__(self, stored_password):
        self.stored_password = stored_password

    def authenticate(self, credentials):
        if credentials == self.stored_password:
            return "Password authentication successful. Access granted."
        return "Password authentication failed: Incorrect password."

class OTPAuthentication(Authentication):
    def __init__(self, current_otp):
        self.current_otp = current_otp

    def authenticate(self, credentials):
        if credentials == self.current_otp:
            return "OTP authentication successful. Access granted."
        return "OTP authentication failed: Invalid or expired OTP."

class BiometricAuthentication(Authentication):
    def __init__(self, registered_biometric_data):
        self.registered_biometric_data = registered_biometric_data

    def authenticate(self, credentials):
        if credentials == self.registered_biometric_data:
            return "Biometric authentication successful. Access granted."
        return "Biometric authentication failed: Scan did not match."

if __name__ == "__main__":
    auth_methods = [
        PasswordAuthentication("SecurePass123!"),
        OTPAuthentication("859201"),
        BiometricAuthentication("thumbprint_hash_alpha")
    ]

    test_inputs = [
        "SecurePass123!",
        "859201",
        "thumbprint_hash_alpha"
    ]

    for method, credential in zip(auth_methods, test_inputs):
        print(f"Method: {type(method).__name__}")
        print(method.authenticate(credential))
        print()
