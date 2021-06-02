import sys
import collections

def read_pages(pages, visited):
    with open('data/pages.txt') as f:
        for data in f.read().splitlines():
            page = data.split('\t')
            # page[0]: id, page[1]: title
            pages[page[0]] = page[1]
            visited[page[0]] = False

def read_links(links):
    with open('data/links.txt') as f:
        for data in f.read().splitlines():
            link = data.split('\t')
            # link[0]: id (from), links[1]: id (to)
            if link[0] in links:
                links[link[0]].add(link[1])
            else:
                links[link[0]] = {link[1]}

def title_to_id(pages, title):
    for k, v in pages.items():
        if v == title:
            return k

    # titleが存在しない場合
    sys.exit(f'{title} does not exist')

# 終点から遡って経路を生成する
def make_path(pages, start, target, before):
    path = collections.deque()
    id = target
    while id != start:
        path.appendleft(pages[id])
        path.appendleft('>')
        id = before[id]
    
    path.appendleft(pages[start])
    return path
    
def bfs(pages, links, visited, start, target):
    before = {} # どこから来たのかを保存する辞書
    # queue
    container = collections.deque()
    container.append(start)
    
    while container: # containerが空でない間
        v = container.popleft()
        visited[v] = True
        if v == target:
            path = make_path(pages, start, target, before)
            return path
        
        if v in links:
            for next_id in links[v]:
                if visited[next_id] == False:
                    container.append(next_id)
                    before[next_id] = v
                
    return False

def main():
    pages = {}
    links = {}
    visited = {}
    read_pages(pages, visited)
    read_links(links)

    page1, page2 = input().split()
    # idに変換
    id1 = title_to_id(pages, page1)
    id2 = title_to_id(pages, page2)
    
    path = bfs(pages, links, visited, id1, id2)
    if path == False:
        print('No path')
    else:
        print(*path)
    
if __name__ == '__main__':
  main()