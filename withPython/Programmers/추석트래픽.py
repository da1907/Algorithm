import datetime

def solution(lines):
    end_times, start_times = [], []

    for line in lines:
        tmp = line.split()

        # et = 요청이 끝난 연월일시, dur = 요청이 처리되기까지의 시간
        et, dur = "".join(tmp[0] + "T" + tmp[1]), float(tmp[2][:-1])
        print(et, dur)

        # datetime 형태로 변환
        et = datetime.datetime.fromisoformat(et)
        dur = datetime.timedelta(seconds=dur)

        # 각 배열에 저장.
        end_times.append(et)
        start_times.append(et-dur+datetime.timedelta(seconds=0.001))

    # 시작한 시간과 끝난 시간의 배열을 합친다.
    # (처리량이 변화할 때는 새 요청이 들어올 때 / 요청이 끝날 때 뿐이므로)
    total = start_times + end_times

    # 윈도우 기준 = 1초
    sec = datetime.timedelta(seconds=1)
    answer = 0
    for starts in total:
        result = 0

        for i in range(len(end_times)):
            # 해당 로그 기준으로 1초 안에 다른 요청이 완료되었거나, 다른 요청이 새로 들어온 경우
            if starts <= end_times[i] < starts + sec or starts <= start_times[i] < starts+sec:
                result += 1

            # 아니면, 해당 로그 이전에 요청이 들어와서 1초 안에 요청이 끝나지 않은 경우.
            # 1초 윈도우 전체가 포함된 경우를 말함.
            elif start_times[i] <= starts and end_times[i] >= starts + sec:
                result += 1

        if answer < result:
            answer = result
        print("total", total)
        print(et, dur)
        print(end_times, start_times)


    return answer


lines =  ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))
