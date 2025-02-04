import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(r"serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': " ",
})


ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Avinash yadav",
            "branch": "IT-A",
            "starting_year": 2023,
            "total_attendance": 0,
            "standing": "A",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Raj Maurya",
            "branch": "IT-A",
            "starting_year": 2023,
            "total_attendance": 0,
            "standing": "C",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Amitabh chaturvedi",
            "branch": "IT-A",
            "starting_year": 2023,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)