from app import app, db
from app.models.modelsUser import *


db.create_all()

admin= UsrMng_Access(quaUSERNAME='carlo', quaPASSWORD='ajhaj')
guest= UsrMng_Access(quaUSERNAME='emanuele', quaPASSWORD='ajhaj')

db.session.add(admin)
db.session.add(guest)
db.session.commit()

everyone = UsrMng_Access.query.all()
print(str(everyone))
app.run(debug=True)
