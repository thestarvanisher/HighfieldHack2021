import spacy
import nltk
from nltk.corpus import wordnet
from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize


class Node:
    '''
    Node for the tree
    '''

    is_root = None
    val = None
    weight = None
    children = None

    is_negated = None

    def __init__(self, val, weight, is_root):
        self.val = val
        self.weight = weight
        self.is_root = is_root
        self.children = []
        self.is_negated = False


    def addChild(self, node):
        self.children.append(node)

    def getData(self):
        return self.val
    
    def getChildren(self):
        return self.children

class Tree:
    '''
    The tree for the sentences
    '''

    root = None
    weights = {
        "root":6.0, #0.9,
        "root_aux":5.0, #30.5,
        "aux": 4.0,
        "nsubj": 5.0, #0.8,
        "dobj": 4.5, #0.7,
        "advmod": 4.5,#0.7,
        "acomp": 4.5, #0.7
        "amod": 2.0,
    }

    def __init__(self):
        pass

    def addNode(self, token, node, weight=1.0):
        a = Node(val=token, weight=weight, is_root=False)
        node.addChild(a)
        return a
    
    def addRoot(self, token, weight=5.0):
        self.root = Node(val=token, weight=weight, is_root=True)
        return self.root

    def getRoot(self):
        return self.root

    def getWeigth(self, token, parent=None):
        if token.dep_ == "ROOT":
            if token.pos_ == "AUX":
                return self.weights['root_aux']
            else:
                return self.weights['root']
        else:
            if token.dep_ == "neg":
                parent.is_negated = True
                return 0.0
            elif token.dep_ == "nsubj":
                if parent.getData().dep_ == "ROOT":
                    return self.weights['nsubj']
                else:
                    return self.weights['nsubj']
            elif token.dep_ == "acomp":
                if token.pos_ == "ADJ":
                    return self.weights['acomp']
            elif token.dep_ == "dobj":
                if token.pos_ == "NOUN":
                    return self.weights['dobj']
                else:
                    return 0.0
            elif token.dep_ == "advmod":
                if token.pos_ == "ADJ":
                    return self.weights['advmod']
            elif token.dep_ == "amod":
                if token.pos_ == "ADJ":
                    return self.weights['amod']
            elif token.dep_ == "aux":
                if token.pos_ == "AUX":
                    return self.weights['aux']
            else:
                return 0.0



    def buildChildren(self, token, parent):
        
        w = self.getWeigth(token, parent)
        
        n = self.addNode(token, parent, w)

        for i in n.getData().children:
            self.buildChildren(i, n)
    
    def buildTree(self, token):
        root = token
        weight = 5.0
        if root.pos_ == "AUX":
            weight = 3.0
        
        weight = self.getWeigth(root)

        n = self.addRoot(root, weight)

        for i in n.getData().children:
            self.buildChildren(i, n)
    
    def printTree(self):
        print(self.getRoot().getData().text)

        ls_old = []
        ls_new = []

        ls_old.append(self.getRoot())

        while len(ls_old) > 0:
            e = ls_old.pop(0)

            for j in e.getChildren():
                ls_new.append(j)
            
            for s in ls_new:
                print("(", s.getData().text, " ", s.weight, ")", end=", ")
            
            print()
            print("--------------")

            ls_old = ls_new
            ls_new = []
    


class CompareStrings:
    '''
    Compare the strings. Compare by a trained model and
    then by custom wordnet.
    '''

    nlp = None
    weights = {
        "root": 0.8,
        "verb": 0.7,
        "noun": 0.6,
        }

    tree_new = None
    trees = []

    model = None

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.tree = Tree()
        self.model = Doc2Vec.load("compare_model.model")


    def prepareTrees(self, target="", old=[]):
        s1 = self.nlp(target)
        rt = None
        for token in s1:
            if token.dep_ == "ROOT":
                rt = token
                break
        self.tree_new = Tree()
        self.tree_new.buildTree(rt)


        for j in old:
            s2 = self.nlp(j)

            rt = None
            for token in s2:
                if token.dep_ == "ROOT":
                    rt = token
                    break
            tr = Tree()
            tr.buildTree(rt)
            self.trees.append(tr)

    def compareStrings(self, target="", old=[]):
        
        self.prepareTrees(target, old)

        self.tree_new.printTree()

        res = [0.0]*len(old)
        
        for i in range(len(res)):
            res[i] += self.compareThroughModel(target, old[i])
        
        res1 = []
        for j in self.trees:
            res1.append(self.compare(self.tree_new, j))
        
        for i in range(len(res)):
            if res[i] > 0.66 and res[i] > res1[i]:
                res[i] = res1[i]
            else:
                res[i] = (res[i] + res1[i]) / 2

        return res



    def compare(self, target, old_t):
        
        l1_old = []
        l1_new = []
        l2_old = []
        l2_new = []

        l1_old.append(target.getRoot())
        l2_old.append(old_t.getRoot())

        score = 0.0
        cnt = 0

        ran = False

        while len(l1_old) > 0 and len(l2_old) > 0:

            if ran == False:
                l1_new = l1_old
                l2_new = l2_old
                ran = True
            else:
                s1 = l1_old.pop(0)
                s2 = l2_old.pop(0)

                for j in s1.getChildren():
                    l1_new.append(j)
                for j in s2.getChildren():
                    l2_new.append(j)

            
            for i in l1_new:
                for j in l2_new:
                    if i.getData().dep_ == j.getData().dep_ or (i.getData().pos_ == "ADJ" and j.getData().pos_ == "ADJ"):

                        if len(wordnet.synsets(i.getData().text)) == 0 or len(wordnet.synsets(j.getData().text)) == 0:
                            continue
                        mx = 0.0
                        for k in wordnet.synsets(i.getData().text):
                            for p in wordnet.synsets(j.getData().text):
                                if k.pos() != p.pos():
                                    continue
                                s = k.wup_similarity(p)
                                if s != None:
                                    if s >= mx:
                                        mx = s

                        similarity = mx

                        w1 = 1.0
                        w2 = 1.0
                        if i.weight != None:
                            w1 = i.weight
                        if j.weight != None:
                            w2 = j.weight
                        
                        w = 0.0

                        if (i.is_negated and j.is_negated) or (i.is_negated == False and j.is_negated == False):
                            w = max(w1, w2)
                        else:
                            w = 1/max(w1, w2)
                        cnt += max(w1, w2)

                        score = score + similarity*w

            
            l1_old = l1_new
            l2_old = l2_new
            l1_new = []
            l2_new = []
            
        score = score / cnt

        return score
        
    def compareThroughModel(self, target, old):
        t1 = word_tokenize(target.lower())
        t2 = word_tokenize(old.lower())

        return self.model.wv.n_similarity(t1,t2)
        
