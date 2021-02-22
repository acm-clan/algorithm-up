import leetcode
import json
import util

leet = leetcode.Leetcode()

def show_menu():
    print("1 help: show help")
    print("2 leetcode tag")

def get_problem_id(data):
    id = data['data']['question']['questionId']
    fid = data['data']['question']['questionFrontendId']
    if util.is_int(fid):
        id = fid
    return id

def check_leetcode_tags():
    print("--------------tags begin-------------")
    problems = leet.get_all_problems()
    all_tags = []

    for k in problems:
        j = json.loads(problems[k])
        tags = j['data']['question']['topicTags']
        for t in tags:
            all_tags.append(t['slug'])
    all_tags = list(dict.fromkeys(all_tags))
    all_tags.sort()
    print('\n'.join([str(item) for item in all_tags]))
    print("--------------tags end-------------")

def check_leetcode_tag(s):
    if len(s) <= 0:
        check_leetcode_tags()
        return
    tag = s[0].lower()
    problems = leet.get_all_problems()

    datas = []
    for k in problems:
        j = json.loads(problems[k])
        tags = j['data']['question']['topicTags']
        if len(tags) > 0:
            for t in tags:
                if t['slug'] == tag:
                    datas.append(j)
                    break
    # 
    ids = []
    for k in datas:
        id = get_problem_id(k)
        if int(id) < 100000:
            ids.append(int(id))
    ids.sort()
    print(' '.join([str(item) for item in ids ]))

def check_leetcode(s):
    if s[0] != "leetcode":
        return
    if s[1] == "tag":
        check_leetcode_tag(s[2:])

def main():
    print("This is a query system.")
    show_menu()
    while True:
        s = input().strip()
        slist = s.split()
        if s == "help":
            show_menu()
        check_leetcode(slist)

if __name__ == "__main__":
    main()
    leet.close_db()