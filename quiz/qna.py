'''
    qna.py holds the question and answer pairs to be used in main.py
    question answer pairs are structered like this:
    [[question, [answer1, answer2, ..., answerN]], [question2, [answer1, answer2, ..., answerN]]]
    This is so that the questions can be randomized and still be linked to their correct answer(s).
'''

qna = [["1 + 1", ['two', '2']], ['2 + 2', ['four', '4']], ['3 factorial', ['6', 'six']], ['What is the value of Pi(3 d.p.)?', ['3.141', 'three point one four one']], ["Twenty times fifty", ["1000", "one thousand"]], ["Who found Eulers number", ['euler']], ["Does pythagoras' theory work on non-right angle triangles", ['no', 'n']], ['8 * 8', ['64', 'sixty-four']], ['e^(pi * i) equals', ['-1', 'minus one']], ['sqrt(-1)', ['i']], ['1 / 0', ['undefined', 'unknown']]]
