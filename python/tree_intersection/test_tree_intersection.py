from tree_intersection import tree_intersection,Binary_Search_Tree,Tnode


def test_tree_intersection_empty_trees():
    t1 = Binary_Search_Tree()
    t2 = Binary_Search_Tree()
    assert tree_intersection(t1, t2) == []

def test_tree_intersection_one_empty_tree():
    tn1 = Tnode(10)
    t1 = Binary_Search_Tree(tn1)
    t1.add(17)
    t1.add(9)
    t1.add(11)
    t1.add(30)

    t2 = Binary_Search_Tree()
    assert tree_intersection(t1, t2) == []


def test_tree_intersection_no_common_values():
    tn1 = Tnode(10)
    t1 = Binary_Search_Tree(tn1)
    t1.add(17)
    t1.add(9)
    t1.add(11)
    t1.add(30)

    tn2 = Tnode(40)
    t2 = Binary_Search_Tree(tn2)
    t2.add(7)
    t2.add(9)
    t2.add(11)

    assert tree_intersection(t1, t2) == ['9', '11']


def test_tree_intersection_with_common_values():
    tn1 = Tnode(10)
    t1 = Binary_Search_Tree(tn1)
    t1.add(17)
    t1.add(9)
    t1.add(11)
    t1.add(30)

    tn2 = Tnode(10)
    t2 = Binary_Search_Tree(tn2)
    t2.add(7)
    t2.add(9)
    t2.add(11)
    t2.add(40)

    assert tree_intersection(t1, t2) == ['10', '9', '11']


def test_tree_intersection_with_duplicate_common_values():
    tn1 = Tnode(10)
    t1 = Binary_Search_Tree(tn1)
    t1.add(17)
    t1.add(9)
    t1.add(9)
    t1.add(11)
    t1.add(30)

    tn2 = Tnode(10)
    t2 = Binary_Search_Tree(tn2)
    t2.add(7)
    t2.add(9)
    t2.add(11)
    t2.add(40)

    assert tree_intersection(t1, t2) == ['10', '9', '11']

def test_tree_intersection_with_all_duplicate_common_values():
    tn1 = Tnode(10)
    t1 = Binary_Search_Tree(tn1)
    t1.add(17)
    t1.add(9)
    t1.add(11)
    t1.add(30)

    tn2 = Tnode(10)
    t2 = Binary_Search_Tree(tn2)
    t2.add(17)
    t2.add(9)
    t2.add(11)
    t2.add(30)

    assert tree_intersection(t1, t2) == ['10', '9', '17', '11', '30']

