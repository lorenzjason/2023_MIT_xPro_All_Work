# firebase - backend as a service, BaaS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://activity12-5-a5b81-default-rtdb.firebaseio.com/'
})

# save data
ref = db.reference('py/')
users_ref = ref.child('Rooms')
users_ref.set({
    'DiningRoom': {
        'Sqft': 954,
        'Appliance1': 'Stove'
    },
    'BedRoom': {
        'Sqft': 36,
        'Appliance1': 'Bed'
    }
})

# update data
hopper_ref = users_ref.child('BedRoom')
hopper_ref.update({
    'Appliance2': 'Dresser'
})

# read data
handle = db.reference('py/Rooms/DiningRoom')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())