from app import app, db
from app.models.modelsUser import UsrMng_Access

db.create_all()

admin= UsrMng_Access(quaID='1', quaUSERNAME='carlo', quaPASSWORD='ajhaj', quaEMAIL='fdhfj', quaID_ANAGRAPHIC='3', quaID_PERMISSION='1', quaQUESTIONARIE='4')
guest= UsrMng_Access(quaID='2', quaUSERNAME='emanuele', quaPASSWORD='ajhaj', quaEMAIL='fdhfj', quaID_ANAGRAPHIC='3', quaID_PERMISSION='1', quaQUESTIONARIE='4')

db.session.add(admin)
db.session.add(guest)
db.session.committ()

everyone = UsrMng_Access.query.all()
print(str(everyone))
app.run(debug=True)
