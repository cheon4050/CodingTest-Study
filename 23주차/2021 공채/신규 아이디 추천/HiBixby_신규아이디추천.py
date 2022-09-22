import re
def solution(new_id):
    tmp=new_id.lower()
    tmp = re.sub('[^\w\-.]','',tmp)
    tmp = re.sub('\.+','.',tmp)
    tmp = re.sub('^\.|\.$','',tmp)
    tmp = tmp[:15] if len(tmp) else "a"
    tmp = re.sub('\.$','',tmp)
    while(len(tmp)<3):tmp+=tmp[-1]
    
    answer=tmp
    return answer