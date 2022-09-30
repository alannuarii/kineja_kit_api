from database import Base, engine
from models import Unit, Spesifikasi, Pengusahaan


print('Creating database')

Base.metadata.create_all(engine)

print('Success')