from lxml import html

with open('resources/仙逆人物志.html', 'r', encoding='utf-8') as f:
    content = f.read()

    # 解析HTML内容，将其转换为一个HTML树对象
    document = html.fromstring(content)

    # 解析表头 - xpath表达式：//table/thead/tr/th ： 表示从任意位置开始匹配
    # 解析表头 - xpath表达式：/table/thead/tr/th ： 表示从根节点开始匹配
    th_list = document.xpath('//table/thead/tr/th/text()')
    print(th_list)

    # tr[2] 表示匹配第2个tr标签
    tr2_list = document.xpath('//table/tbody/tr[2]/td/text()')
    print(tr2_list)

    # last() 表示匹配最后一个tr标签
    tr_list = document.xpath('//table/tbody/tr[last()]/td/text()')
    print(tr_list)

    # 解析所有的p标签文本内容
    p_list = document.xpath('//p/text()')
    print(p_list)

    # 解析所有具有class属性的p标签文本内容
    p_class_list = document.xpath('//p[@class]/text()')
    print(p_class_list)