# firebase - backend as a service, BaaS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('Part_4/serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://assignment-module12-8dc90-default-rtdb.firebaseio.com/'
})

# save data
ref = db.reference('py/')
users_ref = ref.child('sales')
users_ref.set({
    'order1': {
        'item': 'Headphones',
        'Price': '499.99'
    },
    'order2': {
        'item': 'Couch',
        'Price': '4599.98'
    }
})

# update data
hopper_ref = users_ref.child('order2')
hopper_ref.update({
    'Delivery_status': 'Delivered'
})

# read data
handle = db.reference('py/sales/order2')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())