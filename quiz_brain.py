import html


class QuizBrain:
    def __init__(self, qs_bank):
        self.qs_num = 0
        self.qs_list = qs_bank
        self.score = 0
        self.qs = None

    def still_has_qs(self):
        return self.qs_num < len(self.qs_list)

    def next_qs(self):
        self.qs = self.qs_list[self.qs_num]
        qs_text = html.unescape(self.qs.text)
        self.qs_num += 1
        return f"Q{self.qs_num}. {qs_text} (True/False?): "
        # self.check_ans(us_ans, qs.ans)

    def check_ans(self, user_ans):
        corr_ans = self.qs.ans
        if user_ans.title() == corr_ans:
            self.score += 1
            return True
        else:
            return False

