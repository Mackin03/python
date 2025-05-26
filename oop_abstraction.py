#Abstraction

#Reduce complexity by hiding unnecessary details.

class EmailService:
    
    def _connect(self):
        print("connecting to email server")
    
    def _authenticate(self):
        print("Authenticating...")

    def send_email(self):
        self._connect()
        self._authenticate
        print("Sending email...")

    def _disconnect(self):
        print("Disconnecting from email server...")

email = EmailService()
email.send_email()
