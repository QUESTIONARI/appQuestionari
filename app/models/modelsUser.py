from app import db

#from modelsQuestionarie import Mng_Questionarie


class UsrMng_Access(db.Model):
    quaID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quaUSERNAME = db.Column(db.String(255), nullable=False)
    quaPASSWORD = db.Column(db.String(255), nullable=False)
    # quaEMAIL= db.Column (db.String(255), nullable=False)
    # quaID_ANAGRAPHIC = db.Column(db.Integer, db.ForeignKey('UsrMng_Anagraphic.quanID'), nullable=False)
    # quaID_PERMISSION = db.Column(db.Integer, db.ForeignKey('UsrMng_Permission.qupID'), nullable=False)
    #quaQUESTIONARIE = db.relationship('Mng_Questionarie', backref='UsrMng_Access', lazy='select')

    # def __init__(self, quaID, quaUSERNAME, quaPASSWORD, quaEMAIL, quaID_ANAGRAPHIC, quaID_PERMISSION, quaQUESTIONARIE):
    #     self.quaID = quaID
    #     self.quaUSERNAME = quaUSERNAME
    #     self.quaPASSWORD = quaPASSWORD
    #     self.quaEMAIL = quaEMAIL
    #     self.quaID_ANAGRAPHIC = quaID_ANAGRAPHIC
    #     self.quaID_PERMISSION = quaID_PERMISSION
    #     self.quaQUESTIONARIE = quaQUESTIONARIE

# class UsrMng_Anagraphic(db.Model):
#     quanID = db.Column (db.Integer, primary_Key=True, autoincrement=True)
#     quanNAME = db.Column (db.String(255), nullable=True)
#     quanSURNAME = db.Column (db.String(255), nullable=True)
#     quanBIRTH_DATE= db.Column (db.DateTime, nullable=True)
#     quanTELEPHONE = db.Column(db.String, nullable=True)
#     quanCITY = db.Column(db.String, nullable=True)
#     quanBIRTH_PLACE = db.Column(db.String, nullable=True)
#     quanGENDER = db.Column(db.String, nullable=True)
#     #quanACCESS = db.relationship('UsrMng_Access', backref = 'UsrMng_Anagraphic', lazy ='select')

# class UsrMng_Permission(db.Model):
#     qupID = db.Column (db.Integer, primary_Key=True, autoincrement=True)
#     qupLEVEL = db.Column (db.String(255), nullable=True)
#     #qupACCESS = db.relationship('UsrMng_Access', backref='UsrMng_Permission', lazy='select')



