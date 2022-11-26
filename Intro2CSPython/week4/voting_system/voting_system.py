import json
import csv

def file_loader(path, file_type):
    if file_type == 'json':
        with open(file=path, mode='r') as data_file:
            votes = json.load(data_file)
    else:
        votes = {}
        with open(path, 'r') as data_file:
            data = csv.reader(data_file)
            votes = {'options' if key == 0 else 'vote_' + str(key):val if key == 0 else [eval(val) for val in val] for (key, val) in enumerate(data)}
            # for key, val in enumerate(data):
            #     if key == 0:
            #         votes['options'] = val
            #     else:
            #         val = [eval(val) for val in val]
            #         votes['vote_' + str(key)] = val
    # print(votes)
    return votes


def clean_votes(data):
    clean = dict(data)
    for key, val in data.items():
        if len(data['options']) != len(val):
            del clean[key]
        if key != 'options':
            if len(set(val)) != len(data['options']):
                del clean[key]
            for v in val:
                if v > len(data['options']) or v == 0:
                    del clean[key]
    # print(clean)
    return clean


def plurality(votes):
    options = votes['options']
    count = [val[0] for key, val in votes.items() if key != 'options']
    winners = {key:None for key in range(1, len(votes['options']) + 1)}
    # result = {key:count.count(i) for i in set(count) for key in set(count)}
    result = {key:None for key in set(count)}
    for i in set(count):
        result[i] = count.count(i)
    sort_result = sorted(result.items(), key=lambda x:x[1], reverse=True)
    sort_result = dict(sort_result).keys()
    for i, j in enumerate(sort_result):
        winners[i+1] = options[j-1]

    # print(count)
    # print(winners)
    # print(sort_result)
    # print(options)
    return winners


def instant_runoff(votes):
    keys = ['id', 'name', 'count']
    # options = [{key+1:val} for (key, val) in enumerate(votes['options'])]
    assets = [{key:(i+1 if key == 'id' else votes['options'][i] if key == 'name' else 0) for key in keys} for i in range(len(votes['options']))]
    del votes['options']

    print(assets)


def condorcet(votes):
    pass


def display_results(plurality_results, instant_runoff_results, condorcet_results):
    pass


def main():
    # data = file_loader('votes/Streaming_False.json', 'json')
    data = file_loader('votes/Streaming_True.csv', 'csv')
    clean = clean_votes(data)
    # plurality(clean)
    instant_runoff(clean)


if __name__ == "__main__":
    main()