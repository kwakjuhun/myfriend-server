from konlpy.tag import Okt

def analysis(text):
    okt = Okt()
    data = okt.pos(text)
    back = {}    
    back['action'] = "검색"
    back['body'] = data
    return back