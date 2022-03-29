from fastbook import load_learner
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

def powerbi_imgdes(img_list):
    path = 'powerBI.pkl'
    learn_inf = load_learner(path)
    descriptions = []
    for img in img_list:
        category,probability,tensor = learn_inf.predict(img)
        descriptions.append(category)
    return descriptions
