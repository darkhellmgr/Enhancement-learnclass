import pyrebase
config = {
    'apiKey': "AIzaSyCkskZ8L8IYap9ss_TvYlJfwYh-tsL5sVg",
    'authDomain': "fs-learnclass.firebaseapp.com",
    'databaseURL': "https://fs-learnclass.firebaseio.com",
    'projectId': "fs-learnclass",
    'storageBucket': "fs-learnclass.appspot.com",
    'messagingSenderId': "495916606300"
}
firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
db = firebase.database()
storage = firebase.storage()