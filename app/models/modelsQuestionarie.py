# from appQuestionari import db
# from modelsUser import *


# class Mng_Questionarie(db.Model):
#     qmqID = db.Column (db.Integer, primary_Key=True)
#     qmqTITLE = db.Column (db.String(255), nullable=False)
#     qmqID_USER = db.Column (db.Integer, db.ForeignKey('UsrMng_Access.quaID'), nullable=False)
#     qmqCREATE_DATE= db.Column (db.DataTime, nullable=False)
#     qmqALLOW_QUESTIONARIE_YN = db.Column(db.Boolean, default=True)
#     qmqQUESTIONS = db.relationship('Mng_Questions', backref='Mng_Questionarie', lazy='select')
#     qmqRESULTS = db.relationship('Mng_Results', backref='Mng_Questionarie', lazy='select')
#     qmqRELATIONS = db.relationship('Mng_Relations', backref='Mng_Questionarie', lazy='select')

# class Mng_Questions(db.Model):

#     qmqqID = db.Column (db.Integer, primary_Key=True)
#     qmqqID_QUESTIONARIE = db.Column (db.Integer, db.ForeignKey('Mng_Questionarie.qmqID'), Nullable=False)
#     qmqqTEXTCONTENT = db.Column (db.Text,Nullable=False)
#     qmqqALLOW_QUESTION_YN = db.Column (db.Boolean, default=True)
#     qmqqANSWERS = db.relationship('Mng_Answers', backref='Mng_Questions', lazy='select')


# class Mng_Answers(db.Model):
#     qmaID = db.Column (db.Integer, primary_Key=True)
#     qmaID_QUESTION = db.Column (db.Integer, db.ForeignKey('Mng_Questions.qmqqID'), Nullable=False)
#     qmaTEXTCONTENT = db.Column (db.Text,Nullable=False)
#     qmaVALUE = db.Column (db.Integer, Nullable=False)
#     qmaALLOW_ANSWER_YN = db.Column (db.Boolean, default=True)

# class Mng_Results(db.Model):
#     qmrID = db.Column (db.Integer, primary_Key=True)
#     qmrID_QUESTIONARIE = db.Column (db.Integer, db.ForeignKey('Mng_Questionarie.qmqID'), Nullable=False)
#     qmrTEXTCONTENT = db.Column (db.Text,Nullable=False)
#     qmrSCORE_RANGE = db.Column (db.Integer, Nullable=False)

# class Mng_Categories(db.Model):
#     qmcID = db.Column (db.Integer, primary_Key=True)
#     qmcNAME = db.Column (db.String(255), Nullable=False)
#     qmcRELATIONS = db.relationship('Mng_Relations', backref='Mng_Categories', lazy='select')

# class Mng_Relations(db.Model):
#     qmrrID = db.Column (db.Integer, primary_Key=True)
#     qmrrID_QUESTIONARIE = db.Column (db.Integer, db.ForeignKey('Mng_Questionarie.qmqID'), Nullable=False)
#     qmrrID_CATEGORY = db.Column (db.Integer, db.ForeignKey('Mng_Categories.qmcID'), Nullable=False)
    






