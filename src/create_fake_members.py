import json
import uuid
from time import time
from datetime import datetime
from faker import Faker

RECORD_COUNT = 20
fake = Faker(locale="NL_nl")


def create_json_file():
    with open('../output/files/fakeMembers.json', 'w', newline='') as jsonfile:
        for i in range(RECORD_COUNT):
            ref = uuid.uuid4()
            date = fake.date_of_birth()
            dt = datetime.fromordinal(date.toordinal())
            birthdate = {'long': int(dt.timestamp()*1000)}
            eventname = {'string': 'MemberSignedUp'}
            firstname = {'string': fake.first_name()}
            lastname = {'string': fake.last_name()}
            city = {'string': fake.city()}
            zip = {'string': fake.postcode()}
            address = {'string': fake.street_address()}
            # birthdate = {'null': None}
            my_json_string = json.dumps({
                'domainEventName': eventname,
                'reference': str(ref),
                'firstName': firstname,
                'lastName': lastname,
                'birthDate': birthdate,
                'city': city,
                'zip': zip,
                'address': address
            })
            newMember = '"' + str(ref) + '"' + ':' + my_json_string + '\n'
            print(newMember)
            jsonfile.write(newMember)

        jsonfile.close()

if __name__ == '__main__':
    start = time()
    create_json_file()
    elapsed = time() - start
    print('created json file time: {}'.format(elapsed))
