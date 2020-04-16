import surprise as surp



if __name__ == "__main__":
    data = surp.Dataset.load_builtin('ml-100k')
    trainset, testset = surp.train_test_split(data, test_size=.25)

    model1 = surp.SVD()
    model2 = surp.NMF()

    surp.cross_validate(model2, trainset, measures=['RMSE', 'MAE'], cv=10, verbose=True)