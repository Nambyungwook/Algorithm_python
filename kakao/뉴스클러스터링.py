def solution(str1, str2):

    exception_string = "0123456789!@#$%^&*()_+=-~`<>,.?/\|;: "

    u_str1 = str1.upper()
    u_str2 = str2.upper()

    tmp_str_1 = []
    tmp_str_2 = []
    for i in range(len(u_str1)):
        tmp_str_1.append(u_str1[i:i+2])
    tmp_str_1.pop(len(u_str1)-1)

    for i in range(len(tmp_str_1)):
        tmp = tmp_str_1[i]
        if any(sym in tmp for sym in exception_string):
            tmp_str_1[i] = None

    #특수문자 제거 상태
    temp_1 = []
    for i in range(len(tmp_str_1)):
        if tmp_str_1[i]!=None:
            temp_1.append(tmp_str_1[i])
    tmp_str_1 = temp_1
    # print(tmp_str_1)

    for i in range(len(u_str2)):
        tmp_str_2.append(u_str2[i:i+2])
    tmp_str_2.pop(len(u_str2) - 1)

    for i in range(len(tmp_str_2)):
        tmp = tmp_str_2[i]
        if any(sym in tmp for sym in exception_string):
            tmp_str_2[i] = None

    # 특수문자 제거 상태
    temp_2 = []
    for i in range(len(tmp_str_2)):
        if tmp_str_2[i] != None:
            temp_2.append(tmp_str_2[i])
    tmp_str_2 = temp_2
    # print(tmp_str_2)

    tmp_str_1_intersection = {}
    tmp_str_2_intersection = {}

    for i in range(len(tmp_str_1)):
        cnt_str2 = 0
        for j in range(len(tmp_str_2)):
            if tmp_str_1[i]==tmp_str_2[j]:
                cnt_str2+=1

        tmp_str_1_intersection[tmp_str_1[i]] = cnt_str2

    for i in range(len(tmp_str_2)):
        cnt_str1 = 0
        for j in range(len(tmp_str_1)):
            if tmp_str_2[i]==tmp_str_1[j]:
                cnt_str1+=1

        tmp_str_2_intersection[tmp_str_2[i]] = cnt_str1

    tmp_intersection = []
    list_str_1_intersection_key = list(tmp_str_1_intersection.keys())
    list_str_2_intersection_key = list(tmp_str_2_intersection.keys())

    if len(list_str_1_intersection_key)>len(list_str_2_intersection_key):
        for i in range(len(list_str_1_intersection_key)):
            for j in range(len(list_str_2_intersection_key)):
                if list_str_1_intersection_key[i]==list_str_2_intersection_key[j]:
                    intersection_num = min(tmp_str_1_intersection[list_str_1_intersection_key[i]], tmp_str_2_intersection[list_str_2_intersection_key[j]])
                    for k in range(intersection_num):
                        tmp_intersection.append(list_str_1_intersection_key[i])
    else:
        for i in range(len(list_str_2_intersection_key)):
            for j in range(len(list_str_1_intersection_key)):
                if list_str_2_intersection_key[i] == list_str_1_intersection_key[j]:
                    intersection_num = min(tmp_str_1_intersection[list_str_1_intersection_key[j]],
                                           tmp_str_2_intersection[list_str_2_intersection_key[i]])
                    for k in range(intersection_num):
                        tmp_intersection.append(list_str_2_intersection_key[i])


    # print(tmp_str_1_intersection)
    # print(tmp_str_2_intersection)
    #
    # print(tmp_intersection)
    #
    # print(len(tmp_str_1))
    #
    # print(len(tmp_str_2))

    if len(tmp_str_1)==0 and len(tmp_str_2)==0:
        answer = int(65536*1)
    else:
        answer = int(65536*(len(tmp_intersection)/(len(tmp_str_1)+len(tmp_str_2)-len(tmp_intersection))))

    return answer

str1 = "aa1+aa2"
str2 = "AAAA12"

print(solution(str1, str2))