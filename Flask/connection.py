import pymysql

conn = pymysql.connect(user='', passwd='', db='')
cur = conn.cursor()


class DatabaseConn:
    def AddPlayer(self, name, link):
        cur.execute("call trivia_lv.Add_player('"+name+"', '"+link+"');")
        conn.commit()

    def AddQuestion(self, level, question, answer, answer_1, answer_2, answer_3):
        cur.execute(
            "call trivia_lv.Add_question(" + level + ", '" + question + "', '" + answer + "', '" + answer_1 + "', '" + answer_2 + "', '" + answer_3 + "');")
        conn.commit()

    def AddPoints(self, player_id, points):
        cur.execute("call trivia_lv.Add_score(" +str(player_id)+ "," +str(points)+ ");")
        conn.commit()

    def DeletePlayer(self, player_id):
        cur.execute("call trivia_lv.Delete_player(" + str(player_id) + ");")
        conn.commit()
        return "Player_Deleted"

    def DeleteQuestion(self, level, question_id):
        cur.execute("call trivia_lv.Delete_question(" + str(level) + "," + str(question_id) + ");")
        conn.commit()
        return "questionDeleted"

    def EditQuestion(self, question_id, question_level, quest, answ, fal1, fal2, fal3):
        cur.execute(
            "call trivia_lv.edit_question("+question_id+", "+question_level+", '"+quest+"', '"+answ+"', '"+fal1+"', '"+fal2+"', '"+fal3+"');")
        conn.commit()
        return "questionDeleted"

    def GetPlayers(self):
        cur.execute("call trivia_lv.Get_players();")
        conn.commit()
        Elist = []
        for col in cur.fetchall():
            invoiceDic = {
                "user_id": col[0],
                "user_name": col[1],
                "score": col[2],
                "avatar": col[3]
            }
            Elist.append(invoiceDic)
        return Elist

    def GetQuestionAnsw(self, level, ids):
        cur.execute("call trivia_lv.Get_question_answer(" + str(level) + "," + str(ids) + ");")
        conn.commit()
        Elist = []
        for col in cur.fetchall():
            invoiceDic = {
                "answer": col[0],
            }
            Elist.append(invoiceDic)
        return Elist

    def GetQuestionsByLvl(self, level):
        cur.execute("call trivia_lv.Get_question_lvl(" + str(level) + ");")
        conn.commit()
        Elist = []
        for col in cur.fetchall():
            invoiceDic = {
                "question_id": col[0],
                "question": col[1],
                "option_1": col[2],
                "option_2": col[3],
                "option_3": col[4],
                "option_4": col[5],
                "level": col[6]
            }
            Elist.append(invoiceDic)
        return Elist
