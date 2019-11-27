from appQuestionari import db


class Questionari_Management_Questionarie(db.Model):
    qmqID = db.Column (db.Integer, primary_Key=True)
    qmqTITLE = db.Column (db.String(255), nullable=False)
    qmqID_USER = db.Column (db.Integer, nullable=False)
    qmqCREATE_DATE= db.Column (db.DataTime, nullable=False)
    qmqALLOW_QUESTIONARIE_YN = db.Column(db.Boolean, default=True)

class Questionari_Management_Questions(db.Model):

    qmqqID = db.Column (db.Integer, primary_Key=True)
    qmqqID_QUESTIONARIE = db.Column (db.Integer, Nullable=False)
    qmqqID_TEXTCONTENT = db.Column (db.Text,Nullable=False)
    qmqqALLOW_QUESTION_YN = db.Column (db.Boolean, default=True)

class Questionari_Management_Answers(db.Model):
    qmaID = db.Column (db.Integer, primary_Key=True)
    qmaID_QUESTION = db.Column (db.Integer, Nullable=False)
    qmaID_TEXTCONTENT = db.Column (db.Text,Nullable=False)
    qmaVALUE = db.Column (db.Integer, Nullable=False)
    qmaALLOW_ANSWER_YN = db.Column (db.Boolean, default=True)

class Questionari_Management_Results(db.Model):
    qmrID = db.Column (db.Integer, primary_Key=True)
    qmrID_QUESTIONARIE = db.Column (db.Integer, Nullable=False)
    qmrID_TEXTCONTENT = db.Column (db.Text,Nullable=False)
    qmrSCORE_RANGE = db.Column (db.Integer, Nullable=False)

class Questionari_Management_Categories(db.Model):
    qmcID = db.Column (db.Integer, primary_Key=True)
    qmcNAME = db.Column (db.String(255), Nullable=False)

class Questionari_Management_Relations(db.Model):
    qmrrID = db.Column (db.Integer, primary_Key=True)
    qmrrID_QUESTIONARIE = db.Column (db.Integer, Nullable=False)
    qmrrID_CATEGORY = db.Column (db.Integer, Nullable=False)
    






