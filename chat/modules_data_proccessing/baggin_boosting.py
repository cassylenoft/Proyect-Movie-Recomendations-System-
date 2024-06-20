from sklearn.ensemble import BaggingClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def baggin_boosting(model_base, x_data, y_data, n_estimators):
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.35, shuffle=True)
    base_model = model_base

    # Aplicar Bagging al modelo base
    bagging_model = BaggingClassifier(base_model, n_estimators=n_estimators)
    bagging_model.fit(x_train, y_train)
    bagging_pred = bagging_model.predict(x_test)
    bagging_accuracy = accuracy_score(y_test, bagging_pred)
    print("Bagging Accuracy:", bagging_accuracy)

    # Aplicar Boosting al modelo base
    boosting_model = GradientBoostingClassifier(n_estimators=n_estimators,loss='log_loss',learning_rate=0.15,max_depth=5) #boosting solo usa random forest 
    boosting_model.fit(x_train, y_train)
    boosting_pred = boosting_model.predict(x_test)
    boosting_accuracy = accuracy_score(y_test,boosting_pred)
    print("Boosting Accuracy:", boosting_accuracy)  