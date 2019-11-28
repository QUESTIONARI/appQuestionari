from appQuestionari import db


class UsrMng_Access(db.Model):
    quaID = db.Column (db.Integer, primary_Key=True, autoincrement=True)
    quaUSERNAME = db.Column (db.String(255), nullable=False)
    quaPASSWORD = db.Column (db.String(255), nullable=False)
    quaEMAIL= db.Column (db.String(255), nullable=False)
    quaID_ANAGRAPHIC = db.Column(db.Integer, db.ForeignKey('UsrMng_Anagraphic.quanID'), nullable=False)
    quaID_PERMISSION = db.Column(db.Integer, db.ForeignKey('UsrMng_Permission.qupID'), nullable=False)

class UsrMng_Anagraphic(db.Model):
    quanID = db.Column (db.Integer, primary_Key=True, autoincrement=True)
    quanNAME = db.Column (db.String(255), nullable=True)
    quanSURNAME = db.Column (db.String(255), nullable=True)
    quanBIRTH_DATE= db.Column (db.DateTime, nullable=True)
    quanTELEPHONE = db.Column(db.String, nullable=True)
    quanCITY = db.Column(db.String, nullable=True)
    quanBIRTH_PLACE = db.Column(db.String, nullable=True)
    quanGENDER = db.Column(db.String, nullable=True)

class UsrMng_Permission(db.Model):
    qupID = db.Column (db.Integer, primary_Key=True, autoincrement=True)
    qupLEVEL = db.Column (db.String(255), nullable=True)



