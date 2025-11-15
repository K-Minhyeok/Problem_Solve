import numpy
def solution(genres, plays):
    info = dict()
    answer = []
    
    # 해시맵에 장르별 재생횟수 저장 후 내림차순 정렬
    for i in range (len(genres)):
        if genres[i] in info.keys():
            info[genres[i]] += plays[i]
        else :
            info[genres[i]] = plays[i]
    
    info = dict(sorted(info.items(), key=lambda x: x[1], reverse=True))
    
    # 각 장르별 순서 정하기
    for genre, _ in info.items():
        indexs = numpy.where(numpy.array(genres) == genre)[0]
        
        #한 장르에 한 곡만 있을 때 처리
        if len(indexs) == 1:
            answer.append(plays.index(plays[indexs[0]]))
            continue
            
        same_gerne = []
        for idx in indexs:
            same_gerne.append(plays[idx])
            
        for i in range(2):
            cand_val = max(same_gerne)
            print(cand_val)
            
            if same_gerne.count(cand_val) > 1 :
                cand_idx = numpy.where(numpy.array(plays) == cand_val)[0]
                answer.append(int(cand_idx[0]))
                answer.append(int(cand_idx[1]))
                break;
            else :
                cand_idx = plays.index(cand_val)
                answer.append(cand_idx)
                
            same_gerne.remove(cand_val)
    
    return answer
                          
                        