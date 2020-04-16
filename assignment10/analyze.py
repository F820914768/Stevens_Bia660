import surprise as surp
from surprise.model_selection import train_test_split, cross_validate


if __name__ == "__main__":
    data = surp.Dataset.load_builtin('ml-100k')
    #trainset, testset = train_test_split(data, test_size=.25)

    model1 = surp.SVD()
    model2 = surp.NMF()

    print(cross_validate(model2, data, measures=['RMSE', 'MAE'], cv=10, verbose=True))