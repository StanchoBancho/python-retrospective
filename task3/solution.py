class Person:

    def __init__(self, name, birth_year, gender, mother=None, father=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.mother = mother
        if mother:
            mother.add_child(self)
        self.father = father
        if father:
            father.add_child(self)
        self.person_children = set()

    def add_child(self, child):
        self.person_children.add(child)

    def children(self, gender=None):
        if gender is None:
            return list(self.person_children)
        elif gender == 'M':
            return [x for x in self.person_children if x.gender == 'M']
        elif gender == 'F':
            return [x for x in self.person_children if x.gender == 'F']

    def get_all_sibling(self):
        result = set()
        if hasattr(self, 'mother') and self.mother:
            result = set(self.mother.children())
        if hasattr(self, 'father') and self.father:
            sibling_from_father = set(self.father.children())
            return result.union(sibling_from_father)
        return result

    def get_brothers(self):
        all_siblings = self.get_all_sibling()
        return [x for x in all_siblings if x is not self and x.gender == 'M']

    def get_sisters(self):
        all_siblings = self.get_all_sibling()
        return [x for x in all_siblings if x is not self and x.gender == 'F']

    def is_direct_successor(self, person):
        return person in self.person_children
