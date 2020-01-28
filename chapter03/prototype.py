"""
The Prototype Pattern (原型模式:解决对象拷贝问题)
这是创建模式中的最后一个，用来克隆一个对象，有点像生物学中的有丝分裂。
我们可以使用python内置的copy模块实现。
拷贝分为深拷贝和浅拷贝，深拷贝会递归复制并创建新对象，而浅拷贝会利用引用指向同一个对象.
深拷贝的优点是对象之间互不影响，但是会耗费资源，创建比较耗时；
如果不会修改对象可以使用浅拷贝，更加节省资源和创建时间。

原型模式本质就是克隆对象，所以在对象初始化操作比较复杂的情况下，很实用，能大大降低耗时，提高性能，
因为“不用重新初始化对象，而是动态地获得对象运行时的状态”。

应用特性：
需要大量的基于某个基础原型进行微量修改而得到新原型时使用。
"""
import copy


class Website:
    def __init__(self, name, domain, description, author, **kwargs):
        '''Examples of optional attributes (kwargs): 
           category, creation_date, technologies, keywords.
        '''
        self.name = name
        self.domain = domain
        self.description = description
        self.author = author

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        summary = [
            f'Website "{self.name}"\n',
        ]

        infos = vars(self).items()
        ordered_infos = sorted(infos)
        for attr, val in ordered_infos:
            if attr == 'name':
                continue
            summary.append(f'{attr}: {val}\n')

        return ''.join(summary)


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attrs):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f'Incorrect object identifier: {identifier}')
        obj = copy.deepcopy(found)
        for key in attrs:
            setattr(obj, key, attrs[key])

        return obj


def main():
    keywords = ('python', 'data', 'apis', 'automation')
    site1 = Website('ContentGardening',
                    domain='contentgardening.com',
                    description='Automation and data-driven apps',
                    author='Kamon Ayeva',
                    category='Blog',
                    keywords=keywords)

    prototype = Prototype()
    identifier = 'ka-cg-1'
    prototype.register(identifier, site1)

    site2 = prototype.clone(
        identifier,
        name='ContentGardeningPlayground',
        domain='play.contentgardening.com',
        description='Experimentation for techniques featured on the blog',
        category='Membership site',
        creation_date='2018-08-01')

    # 无须先克隆现有对象，然后再修改新对象，而是可以直接用新参数来创建新对象
    site3 = site1.__class__('name1', 'www', 'desc', 'Joe')

    for site in (site1, site2, site3):
        print(id(site))
        print(site)
    print(f'ID site1 : {id(site1)} != ID site2 : {id(site2)}')


if __name__ == '__main__':
    main()
