"""
The Template Pattern (模板模式：抽象出算法公共部分从而实现代码复用)
Don't repeat yourself. 
模板模式中，把代码中重复的部分抽出来作为一个新的函数，把可变的部分作为函数参数，从而消除代码冗余。
"""
from cowpy import cow

def generate_banner(msg, style): 
    print('-- start of banner --') 
    print(style(msg)) 
    print('-- end of banner --nn') 
    
def dots_style(msg): 
    msg = msg.capitalize() 
    msg = '.' * 10 + msg + '.' * 10 
    return msg 
    
def admire_style(msg): 
    msg = msg.upper() 
    return '!'.join(msg) 
    
def cow_style(msg): 
    msg = cow.milk_random_cow(msg) 
    return msg 
    
def main(): 
    styles = (dots_style, admire_style, cow_style)
    msg = 'happy coding' 
    [generate_banner(msg, style) for style in styles] 
     
if __name__ == "__main__":
    main()
